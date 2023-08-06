#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   fedhf\api\opt\opt.py
@Time    :   2021-11-10 17:20:18
@Author  :   Bingjie Yan
@Email   :   bj.yan.pa@qq.com
@License :   Apache License 2.0
"""

import argparse
import os
import torch


class opts(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser()

        # high priority setting
        self.parser.add_argument('--from_file',
                                 default=None,
                                 help='load config from file.')

        # basic experiment setting
        self.parser.add_argument('--project_name',
                                 default='fedhf',
                                 type=str,
                                 help='using for save result.')
        self.parser.add_argument('--name',
                                 default='experiment',
                                 help='name of the experiment.')
        self.parser.add_argument(
            '--deploy_type',
            default='simulated',
            help='type of deployment. [ simulated, standalone, distributed ]')
        self.parser.add_argument(
            '--dataset',
            default='mnist',
            help='see fedhf/dataset for available datasets')
        self.parser.add_argument('--load_model',
                                 default='',
                                 help='path to pretrained model')
        self.parser.add_argument('--resume',
                                 action='store_true',
                                 help='resume an experiment. '
                                 'Reloaded the optimizer parameter and '
                                 'set load_model to model_last.pth '
                                 'in the exp dir if load_model is empty.')

        # system setting
        self.parser.add_argument(
            '--gpus',
            default='0',
            help='-1 for cpu, use comma for multiple gpus')
        self.parser.add_argument(
            '--num_workers',
            type=int,
            default=0,
            help='dataloader threads. 0 for single-thread.')
        self.parser.add_argument('--seed',
                                 type=int,
                                 default=233,
                                 help='random seed')

        # log setting
        self.parser.add_argument('--use_wandb',
                                 action='store_true',
                                 help='using wandb to store result')
        self.parser.add_argument('--wandb_reinit',
                                 action='store_true',
                                 help='reinit wandb')
        self.parser.add_argument('--log_name',
                                 default='logger',
                                 type=str,
                                 help='logger name')
        self.parser.add_argument('--log_file',
                                 default=None,
                                 type=str,
                                 help='where to save log')
        self.parser.add_argument(
            '--log_level',
            default='debug',
            type=str,
            help='log level, it could be in [ error | warning | info | debug ]'
        )

        # model setting
        self.parser.add_argument(
            '--task',
            type=str,
            default='classification',
            help='type of task, lr | classification | nlp')
        self.parser.add_argument('--model',
                                 type=str,
                                 default='resnet',
                                 help='model name.')

        self.parser.add_argument('--model_pretrained',
                                 type=bool,
                                 default=True,
                                 help='load pretrained model or not')
        self.parser.add_argument('--model_dir',
                                 default='./model',
                                 type=str,
                                 help='path to download model')  # Never used
        self.parser.add_argument('--input_c',
                                 type=int,
                                 default=1,
                                 help='input channel')
        self.parser.add_argument('--image_size',
                                 type=int,
                                 default=224,
                                 help='image_size')
        self.parser.add_argument('--num_classes',
                                 type=int,
                                 default=10,
                                 help='number of classes')
        self.parser.add_argument('--optim',
                                 type=str,
                                 default='adam',
                                 help='optimizer.')
        self.parser.add_argument('--lr',
                                 type=float,
                                 default=1.25e-4,
                                 help='learning rate.')
        self.parser.add_argument('--loss',
                                 type=str,
                                 default='ce',
                                 help='loss function.')

        # training setting
        self.parser.add_argument(
            '--check_point',
            type=str,
            default='50',
            help='when to save the model and result to disk.')
        self.parser.add_argument('--num_clients',
                                 type=int,
                                 default=3,
                                 help='clients number.')
        self.parser.add_argument('--num_local_epochs',
                                 type=int,
                                 default=3,
                                 help='local training epochs.')
        self.parser.add_argument('--batch_size',
                                 type=int,
                                 default=8,
                                 help='batch size')
        self.parser.add_argument('--num_rounds',
                                 type=int,
                                 default=5,
                                 help='server round.')
        self.parser.add_argument('--sampler',
                                 type=str,
                                 default='random',
                                 help='data sample strategy')
        self.parser.add_argument('--selector',
                                 type=str,
                                 default='random_async',
                                 help='client select strategy')
        self.parser.add_argument('--select_ratio',
                                 type=float,
                                 default=0.5,
                                 help='select ratio')
        self.parser.add_argument('--agg',
                                 type=str,
                                 default='fedasync',
                                 help='aggregate strategy')

        self.parser.add_argument('--fedasync_strategy',
                                 type=str,
                                 default='constant',
                                 help='fedasync aggregate strategy')
        self.parser.add_argument('--fedasync_alpha',
                                 type=float,
                                 default=0.5,
                                 help='fedasync aggregate alpha')

        # test setting
        self.parser.add_argument('--test',
                                 action='store_true',
                                 help='test mode')

        # custom dataset
        self.parser.add_argument('--dataset_root',
                                 default='./dataset',
                                 help='custom dataset root')
        self.parser.add_argument('--dataset_download',
                                 type=bool,
                                 default=True,
                                 help='dataset download')
        self.parser.add_argument('--resize',
                                 type=bool,
                                 default=True,
                                 help='resize or not')

    def parse(self, args=''):
        if args == '':
            opt = self.parser.parse_args()
        else:
            opt = self.parser.parse_args(args)

        if opt.from_file:
            opt = self.load_from_file(args)

        opt.gpus_str = opt.gpus
        opt.gpus = [int(gpu) for gpu in opt.gpus.split(',')]
        opt.gpus = [i for i in range(len(opt.gpus))
                    ] if opt.gpus[0] >= 0 else [-1]
        opt.device = torch.device('cuda' if opt.gpus[0] >= 0 else 'cpu')

        opt.num_workers = max(opt.num_workers, 2 * len(opt.gpus))

        # make dirs
        # TODO

        if opt.resume and opt.load_model == '':
            opt.load_model = os.path.join(opt.save_dir, 'model_last.pth')
        return opt

    def load_from_file(self, args):
        # TODO
        pass

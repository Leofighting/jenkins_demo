# -*- coding:utf-8 -*-
__author__ = "leo"

import pytest
import allure


@pytest.fixture(scope="session")
def login():
    print("登录操作")
    step1()
    step2()
    step3()


@allure.step("登陆步骤1：输入账号")
def step1():
    print("输入账号")


@allure.step("登陆步骤1：输入密码")
def step2():
    print("输入密码")


@allure.step("登陆步骤1：点击登录")
def step3():
    print("点击登录")

import pytest
import allure


@allure.step("用例步骤111")
def step1():
    print("用例步骤111")


@allure.step("用例步骤222")
def step2():
    print("用例步骤222")


@allure.step("用例步骤333")
def step3():
    print("用例步骤333")


@allure.feature("功能模块1")
class TestDemo():
    """功能模块描述"""

    @allure.title("测试用例标题1")
    def test1(self, login):
        """用例描述1"""
        step1()

    @allure.story("测试用例story2")
    def test2(self, login):
        """用例描述2"""
        step2()

    @allure.story("测试用例story3")
    def test3(self, login):
        """用例描述3"""
        step1()
        step2()
        step3()
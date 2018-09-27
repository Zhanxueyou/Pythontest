__author__ = 'Administrator'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re


class NewTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://test.news.999ask.com/"

    def test_news(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("资讯首页").click()
        driver.find_element_by_link_text("内　科").click()
        driver.find_element_by_link_text("呼吸内科").click()
        driver.find_element_by_link_text("内　科").click()
        driver.find_element_by_link_text("肾内科").click()
        driver.find_element_by_link_text("内　科").click()
        driver.find_element_by_link_text("神经内科").click()
        driver.find_element_by_link_text("内　科").click()
        driver.find_element_by_link_text("心血管内科").click()
        driver.find_element_by_link_text("内　科").click()
        driver.find_element_by_link_text("消化内科").click()
        driver.find_element_by_link_text("内　科").click()
        driver.find_element_by_link_text("免疫科").click()
        driver.find_element_by_link_text("内　科").click()
        driver.find_element_by_link_text("血液内科").click()
        driver.find_element_by_link_text("内　科").click()
        driver.find_element_by_link_text("内分泌科").click()
        #————————
        driver.find_element_by_link_text("外　科").click()
        driver.find_element_by_link_text("普外科").click()
        driver.find_element_by_link_text("外　科").click()
        driver.find_element_by_link_text("骨科").click()
        driver.find_element_by_link_text("外　科").click()
        driver.find_element_by_link_text("心胸外科").click()
        driver.find_element_by_link_text("外　科").click()
        driver.find_element_by_link_text("神经外科").click()
        driver.find_element_by_link_text("外　科").click()
        driver.find_element_by_link_text("麻醉科").click()
        driver.find_element_by_link_text("外　科").click()
        driver.find_element_by_link_text("显微外科").click()
        driver.find_element_by_link_text("外　科").click()
        driver.find_element_by_link_text("器官移植").click()
        driver.find_element_by_link_text("外　科").click()
        driver.find_element_by_link_text("泌尿外科").click()
        #————————
        driver.find_element_by_link_text("妇产科").click()
        driver.find_element_by_link_text("妇科").click()
        driver.find_element_by_link_text("妇产科").click()
        driver.find_element_by_link_text("产科").click()
        driver.find_element_by_link_text("妇产科").click()
        driver.find_element_by_link_text("计划生育").click()
        driver.find_element_by_link_text("妇产科").click()
        driver.find_element_by_link_text("乳腺疾病").click()
        driver.find_element_by_link_text("妇产科").click()
        driver.find_element_by_link_text("宫颈疾病").click()
        driver.find_element_by_link_text("妇产科").click()
        driver.find_element_by_link_text("妇科整形").click()
        driver.find_element_by_link_text("妇产科").click()
        driver.find_element_by_link_text("子宫疾病").click()
        #————————
        driver.find_element_by_link_text("儿　科").click()
        driver.find_element_by_link_text("小儿内科").click()
        driver.find_element_by_link_text("儿　科").click()
        driver.find_element_by_link_text("小儿外科").click()
        driver.find_element_by_link_text("儿　科").click()
        driver.find_element_by_link_text("多动症").click()
        driver.find_element_by_link_text("儿　科").click()
        driver.find_element_by_link_text("疝气").click()
        driver.find_element_by_link_text("儿　科").click()
        driver.find_element_by_link_text("小儿眼科").click()
        driver.find_element_by_link_text("儿　科").click()
        driver.find_element_by_link_text("耳鼻喉科").click()
        driver.find_element_by_link_text("儿　科").click()
        driver.find_element_by_link_text("重症监护").click()
        driver.find_element_by_link_text("儿　科").click()
        driver.find_element_by_link_text("小儿急诊科").click()
        driver.find_element_by_link_text("儿　科").click()
        driver.find_element_by_link_text("抽动症").click()
        driver.find_element_by_link_text("儿　科").click()
        driver.find_element_by_link_text("口吃").click()
        driver.find_element_by_link_text("儿　科").click()
        driver.find_element_by_link_text("遗尿").click()
        driver.find_element_by_link_text("儿　科").click()
        driver.find_element_by_link_text("营养发育").click()
        #————————
        driver.find_element_by_link_text("中医科").click()
        driver.find_element_by_link_text("中医内科").click()
        driver.find_element_by_link_text("中医科").click()
        driver.find_element_by_link_text("中医外科").click()
        driver.find_element_by_link_text("中医科").click()
        driver.find_element_by_link_text("中医妇科").click()
        driver.find_element_by_link_text("中医科").click()
        driver.find_element_by_link_text("中医儿科").click()
        driver.find_element_by_link_text("中医科").click()
        driver.find_element_by_link_text("中医保健科").click()
        driver.find_element_by_link_text("中医科").click()
        driver.find_element_by_link_text("针灸按摩科").click()
        driver.find_element_by_link_text("中医科").click()
        driver.find_element_by_link_text("中医骨伤科").click()
        #————————
        driver.find_element_by_link_text("皮肤科").click()
        driver.find_element_by_link_text("传染性皮肤病").click()
        driver.find_element_by_link_text("皮肤科").click()
        driver.find_element_by_link_text("其他皮肤病").click()
        #————————

        driver.find_element_by_xpath("//div[@class='nav_bj']/ul/li/p/a[@href='/bjys/']").click()
        driver.find_element_by_link_text("健康饮食").click()
        driver.find_element_by_xpath("//div[@class='nav_bj']/ul/li/p/a[@href='/bjys/']").click()
        driver.find_element_by_link_text("生活习惯").click()
        driver.find_element_by_xpath("//div[@class='nav_bj']/ul/li/p/a[@href='/bjys/']").click()
        driver.find_element_by_link_text("人体常识").click()
        driver.find_element_by_xpath("//div[@class='nav_bj']/ul/li/p/a[@href='/bjys/']").click()
        driver.find_element_by_link_text("戒烟戒酒").click()
        driver.find_element_by_xpath("//div[@class='nav_bj']/ul/li/p/a[@href='/bjys/']").click()
        driver.find_element_by_link_text("两性保健").click()
        #————————
        driver.find_element_by_link_text("整形美容").click()
        driver.find_element_by_link_text("美容外科").click()
        driver.find_element_by_link_text("整形美容").click()
        driver.find_element_by_link_text("鼻整形").click()
        driver.find_element_by_link_text("整形美容").click()
        driver.find_element_by_link_text("乳房整形").click()
        driver.find_element_by_link_text("整形美容").click()
        driver.find_element_by_link_text("眼睑整形").click()
        driver.find_element_by_link_text("整形美容").click()
        driver.find_element_by_link_text("整形外科").click()
        driver.find_element_by_link_text("整形美容").click()
        driver.find_element_by_link_text("烧伤整形科").click()
        driver.find_element_by_link_text("整形美容").click()
        driver.find_element_by_link_text("疤痕修复").click()
        driver.find_element_by_link_text("整形美容").click()
        driver.find_element_by_link_text("微整形").click()
        #————————
        driver.find_element_by_link_text("精神心理").click()
        driver.find_element_by_link_text("失眠").click()
        driver.find_element_by_link_text("精神心理").click()
        driver.find_element_by_link_text("抑郁").click()
        driver.find_element_by_link_text("精神心理").click()
        driver.find_element_by_link_text("精神分裂").click()
        driver.find_element_by_link_text("精神心理").click()
        driver.find_element_by_link_text("焦虑").click()
        driver.find_element_by_link_text("精神心理").click()
        driver.find_element_by_link_text("强迫症").click()
        driver.find_element_by_link_text("精神心理").click()
        driver.find_element_by_link_text("成瘾医学").click()
        driver.find_element_by_link_text("精神心理").click()
        driver.find_element_by_link_text("精神科综合").click()
        driver.find_element_by_link_text("精神心理").click()
        driver.find_element_by_link_text("心理科综合").click()
        #————————
        driver.find_element_by_link_text("五官科").click()
        driver.find_element_by_link_text("耳鼻喉科").click()
        driver.find_element_by_link_text("五官科").click()
        driver.find_element_by_link_text("眼科").click()
        driver.find_element_by_link_text("五官科").click()
        driver.find_element_by_link_text("口腔科").click()
        #————————
        driver.find_element_by_link_text("传染科").click()
        driver.find_element_by_link_text("性病科").click()
        driver.find_element_by_link_text("传染科").click()
        driver.find_element_by_link_text("肝病").click()
        driver.find_element_by_link_text("传染科").click()
        driver.find_element_by_link_text("结核病").click()
        driver.find_element_by_link_text("传染科").click()
        driver.find_element_by_link_text("寄生虫疾病").click()
        driver.find_element_by_link_text("传染科").click()
        driver.find_element_by_link_text("狂犬病").click()
        driver.find_element_by_link_text("传染科").click()
        driver.find_element_by_link_text("流行性腮腺炎").click()
        #————————
        driver.find_element_by_link_text("肿瘤科").click()
        driver.find_element_by_link_text("血管瘤").click()
        driver.find_element_by_link_text("肿瘤科").click()
        driver.find_element_by_link_text("腹部肿瘤").click()
        driver.find_element_by_link_text("肿瘤科").click()
        driver.find_element_by_link_text("胸部肿瘤").click()
        driver.find_element_by_link_text("肿瘤科").click()
        driver.find_element_by_link_text("颅脑肿瘤").click()
        driver.find_element_by_link_text("肿瘤科").click()
        driver.find_element_by_link_text("皮肤癌").click()
        driver.find_element_by_link_text("肿瘤科").click()
        driver.find_element_by_link_text("鼻咽癌").click()
        driver.find_element_by_link_text("肿瘤科").click()
        driver.find_element_by_link_text("淋巴癌").click()
        driver.find_element_by_link_text("肿瘤科").click()
        driver.find_element_by_link_text("肿瘤放疗").click()
        driver.find_element_by_link_text("肿瘤科").click()
        driver.find_element_by_link_text("其他").click()
        driver.find_element_by_link_text("肿瘤科").click()
        driver.find_element_by_link_text("妇科肿瘤").click()
        driver.find_element_by_link_text("肿瘤科").click()
        driver.find_element_by_link_text("肿瘤化疗").click()
        #————————
        driver.find_element_by_link_text("中医减肥").click()
        driver.find_element_by_link_text("减肥").click()
        driver.find_element_by_link_text("中医减肥").click()
        driver.find_element_by_link_text("运动知识").click()
        driver.find_element_by_link_text("中医减肥").click()
        driver.find_element_by_link_text("健身健美").click()
        #————————
        driver.find_element_by_link_text("子女教育").click()
        driver.find_element_by_link_text("育儿").click()
        driver.find_element_by_link_text("子女教育").click()
        driver.find_element_by_link_text("学前教育").click()
        driver.find_element_by_link_text("子女教育").click()
        driver.find_element_by_link_text("子女入学").click()
        driver.find_element_by_link_text("子女教育").click()
        driver.find_element_by_link_text("子女能力培养").click()
        #————————








if __name__ == "__main__":
    unittest.main()
#coding=utf-8

from  pages.base_page import BasePage
import time

aa='''渠道业务管理'''#进入渠道业务管理
bb='''业务办理'''
cc='''渠道新建'''
dd='''渠道变更'''
ee='''渠道迁址'''
ff='''渠道关停'''
gg='''渠道过户'''
hh='''渠道增机'''
ii='''渠道退机'''
jj='''渠道移机'''
kk='''销售权限'''
ll='''费率调整'''
mm='''资源采购'''
nn='''资源申请'''
oo='''资源发放'''
pp='''资源调拨'''
qq='''资源报废'''



class business_process(BasePage):
    def jump(self):
        '''跳转到渠道业务办理页面'''
        self.get_text_accurate(aa).click()
        self.get_text_accurate(bb).click()
        time.sleep(2)

    def jump_channelnewbuilt(self):
        '''渠道新建'''
        self.jump()
        self.get_text_accurate(cc).click()
        time.sleep(1)

    def jump_channelchange(self):
        '''渠道变更'''
        self.jump()
        self.get_text_accurate(dd).click()
        time.sleep(1)

    def jump_channelrelocate(self):
        '''渠道迁址'''
        self.jump()
        self.get_text_accurate(ee).click()
        time.sleep(1)

    def jump_channelShutdown(self):
        '''渠道关停'''
        self.jump()
        self.get_text_accurate(ff).click()
        time.sleep(1)

    def jump_channelTransfer(self):
        '''渠道过户'''
        self.jump()
        self.get_text_accurate(gg).click()
        time.sleep(1)

    def jump_channelAddmachine(self):
        '''渠道增机'''
        self.jump()
        self.get_text_accurate(hh).click()
        time.sleep(1)

    def jump_channelback(self):
        '''渠道退机'''
        self.jump()
        self.get_text_accurate(ii).click()
        time.sleep(1)

    def jump_channelMove (self):
        '''渠道移机'''
        self.jump()
        self.get_text_accurate(jj).click()
        time.sleep(1)

    def jump_Salesauthority(self):
        '''销售权限'''
        self.jump()
        self.get_text_accurate(kk).click()
        time.sleep(1)

    def jump_RateAdjustment(self):
        '''费率调整'''
        self.jump()
        self.get_text_accurate(ll).click()
        time.sleep(1)

    def jump_ResourceProcurement(self):
        '''资源采购'''
        self.jump()
        self.get_text_accurate(mm).click()
        time.sleep(1)

    def jump_ResourceApplication(self):
        '''资源申请'''
        self.jump()
        self.get_text_accurate(nn).click()
        time.sleep(1)

    def jump_ResourceProvide(self):
        '''资源发放'''
        self.jump()
        self.get_text_accurate(oo).click()
        time.sleep(1)

    def jump_ResourceAllocation(self):
        '''资源调拨'''
        self.jump()
        self.get_text_accurate(pp).click()
        time.sleep(1)

    def jump_ResourceScrapping(self):
        '''资源报废'''
        self.jump()
        self.get_text_accurate(qq).click()
        time.sleep(1)


;�����ϴ����ڣ���ȡ���㣩
;ControlFocus("title","text",controlID) Edit1=Edit instance 1
ControlFocus("��", "","Edit1")
; �����ϴ����ڳ��ֵĳ�ʱʱ��
WinWait("[CLASS:#32770]","",10)
; �����ļ�·��
ControlSetText("��", "", "Edit1", "D:\genlot_vlt\pages\Business_management\Basic_Infomanagement\upload\dog.jpg")
Sleep(2000)
; �������水ť
ControlClick("��", "","Button1");
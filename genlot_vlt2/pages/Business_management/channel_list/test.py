#coding=utf-8
from db.oracle_db import Oracle
import os
def teat():
    sql = '''SELECT t.ins_id AS insId,
    	t.ins_name AS insName,
    	d.channel_type AS channelType,
    	d.channel_level_id,
    	( SELECT tcgi.ch_level_name FROM t_channel_grade_info tcgi WHERE tcgi.ch_grade_id = d.channel_level_id ) channelLevelName,
    	c.corporate_name corporateName,
    	d.create_by createBy,
    	d.create_time createTime,
    	d.channel_no AS channelNo,
    	d.buy_card_limit buyCardLimit,
    	d.try_card_limit tryCardLimit,
    	d.recharge_count rechargeCount,
    	d.channel_address AS channelAddress,
    	d.longitude,
    	d.latitude,
    	d.region_code regionCode,
    	d.attach_id attachId
    FROM
    	t_channel_info d
    	LEFT JOIN t_partner c ON d.partner_id = c.id
    	INNER JOIN t_ins_info t ON d.ins_id = t.ins_id
    WHERE d.channel_no = '6302009999'  '''

    t=Oracle()
    kk=t.run_sql_dir(sql)
    print kk
    # for i in kk:
    i=list(kk[0])
    print i
    print i[1]

teat()










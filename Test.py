#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import requests
requests.packages.urllib3.disable_warnings()
import cobra.mit.access
import cobra.mit.session as session
import cobra.mit.request
import cobra.mit.session
from tabulate import tabulate
import time

import datetime
from Tkinter import *
import MySQLdb


def main():


	"""DB connetion and insert test"""
	db = MySQLdb.connect('127.0.0.1', 'root', 'Will9455', 'Cisco_Aci')
	cursor = db.cursor()

	mo = cobra.mit.access
	aci_address = 'http://10.124.4.101'
	mo_dir = mo.MoDirectory(session.LoginSession(aci_address, 'admin', 'Cisco123'))
	mo_dir.login()
	clAcPath = cobra.mit.access.ClassQuery('dbgAcTrail')
	dbgAcPath_objlist = mo_dir.query(clAcPath)

	while TRUE:
		for i in dbgAcPath_objlist:
			sql = "INSERT INTO acTrail(dn," \
				  " dropPkt," \
				  " trnstNodeId," \
				  " dropPktPercentage," \
				  " dstNodeId," \
				  " excessPkt," \
				  " excessPktPercentage," \
				  " pathType," \
				  " rxPkt," \
				  " srcNodeId," \
				  " suspect," \
				  " totDropPkt," \
				  " totDropPktPercentage," \
				  " totExcessPkt," \
				  " totExcessPktPercentage," \
				  " totRxPkt," \
				  " totTxPkt," \
				  " txPkt," \
				  " rn ) VALUES('%s'," \
				  " '%s'," \
				  " '%s'," \
				  " '%s'," \
				  " '%s'," \
				  " '%s'," \
				  " '%s'," \
				  " '%s'," \
				  " '%s'," \
				  " '%s'," \
				  " '%s'," \
				  " '%s'," \
				  " '%s'," \
				  " '%s'," \
				  " '%s'," \
				  " '%s'," \
				  " '%s'," \
				  " '%s'," \
				  " '%s') " % (i.dn,
							   i.dropPkt,
							   i.trnstNodeId,
							   i.dropPktPercentage,
							   i.dstNodeId,
							   i.excessPkt,
							   i.excessPktPercentage,
							   i.pathType,
							   i.rxPkt,
							   i.srcNodeId,
							   i.suspect,
							   i.totDropPkt,
							   i.totDropPktPercentage,
							   i.totExcessPkt,
							   i.totExcessPktPercentage,
							   i.totRxPkt,
							   i.totTxPkt,
							   i.txPkt,
							   i.rn )
		cursor.execute(sql)
		db.commit()
		time.sleep(1)



	"""draw table test"""
# 	mo = cobra.mit.access
# 	apicurl = 'http://10.124.4.101'
# 	mo_dir = mo.MoDirectory(session.LoginSession(apicurl, 'admin', 'Cisco123'))
# 	mo_dir.login()
#
# 	for i in range(1, 30):
# 		if i <= 30:
# 			time.sleep(2)
# 		y = i + 1
# 		topology(i, mo_dir)
# 		table(i, mo_dir)
# 		table_1(i, mo_dir)
#
#
# def topology(i, mo):
# 	topology = cobra.mit.access.ClassQuery('dbgAcTrailRx')
# 	fabricTrail_objlist = mo.query(topology)
# 	dbgAclist_0 = []
# 	now = datetime.datetime.now()
# 	for n in fabricTrail_objlist:
# 		row_1 = [
# 			n.dn,
# 			n.dropP,
# 			n.admitB,
# 			n.admitTotP,
# 			# n.dropPkt,
# 			# n.totDropPkt,
# 			# n.totDropPktPercentage,
# 			now.strftime('%Y-%m-%d %H:%M:%S'),
# 		]
# 		dbgAclist_0.append(row_1)
# 	print tabulate(sorted(dbgAclist_0), tablefmt='grid',
# 				   headers=["Path", "DropPackets", "admitted packages", "admitted Total packages", "Time"])
# 	print '\n\n\n\n'
# 	return
#
#
# def table(i, mo):
# 	clAcPath = cobra.mit.access.ClassQuery('fabricTrail')
# 	dbgAcPathA_objlist = mo.query(clAcPath)
# 	dbgAclist = []
# 	now = datetime.datetime.now()
#
# 	for m in dbgAcPathA_objlist:
# 		if "101" in str(m.rn) and "102" in str(m.rn):
# 			dbgAclist.append(str(m.rn))
#
# 	print dbgAclist
# 	print '\n\n\n\n'
# 	return
#
#
# def table_1(i, mo):
# 	clAcPath = cobra.mit.access.ClassQuery('dbgAcTrail')
# 	dbgAcPathA_objlist = mo.query(clAcPath)
# 	dbgAclist = []
# 	now = datetime.datetime.now()
#
# 	for c in dbgAcPathA_objlist:
# 		# if int(m.dropPkt) != 0:
# 		row_2 = [
# 			c.dn,
# 			c.totRxPkt,
# 			c.totTxPkt,
# 			now.strftime('%Y-%m-%d %H:%M:%S'),
# 		]
# 		dbgAclist.append(row_2)
#
# 	print tabulate(dbgAclist, tablefmt='grid', headers=["Path", "Total_Rx", "Total_Tx", "Time"])
# 	print '\n\n\n\n'
# 	return



if __name__ == '__main__':
	main()

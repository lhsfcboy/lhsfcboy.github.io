#!/bin/sh

DSTSV1="c101"
DSTSV2="c102"
REMOTE_CMD_kill_client="ps -ef | grep fix-demo-tradeclient | kill \`awk '{ print \$2 }'\` 2>/dev/null"
REMOTE_CMD_kill_OMS="ps -ef | grep fix-demo-oms         | kill \`awk '{ print \$2 }'\` 2>/dev/null"
REMOTE_CMD_kill_venue="ps -ef | grep fix-demo-exchange    | kill \`awk '{ print \$2 }'\` 2>/dev/null"
#echo $REMOTE_CMD

REMOTE_CMD_boot_client="nohup /root/kra/bin/fix-demo-tradeclient > /dev/null 2>&1  &"
REMOTE_CMD_boot_OMS="nohup /root/kra/bin/fix-demo-oms > /dev/null 2>&1  &"
REMOTE_CMD_boot_venue="nohup /root/kra/bin/fix-demo-exchange-sim > /dev/null 2>&1 &"

echo $REMOTE_CMD_boot_client

ssh $DSTSV1 $REMOTE_CMD_kill_client
ssh $DSTSV2 $REMOTE_CMD_kill_OMS
ssh $DSTSV1 $REMOTE_CMD_kill_venue

ssh $DSTSV1 "$REMOTE_CMD_boot_venue"
ssh $DSTSV2 "$REMOTE_CMD_boot_OMS"
ssh $DSTSV1 "$REMOTE_CMD_boot_client"



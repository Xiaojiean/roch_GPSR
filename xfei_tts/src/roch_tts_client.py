#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import actionlib

from xfei_tts.msg import XFeiTTSAction
from xfei_tts.msg import XFeiTTSGoal
# from xfei_tts.msg import XFeiTTSFeedback
# from xfei_tts.msg import XFeiTTSResult

def text_to_speech(speech_str):
    rospy.init_node("xfei_tts_client", anonymous=False)

    tts_action_client = actionlib.SimpleActionClient('xfei_tts_action', XFeiTTSAction)
    tts_action_client.wait_for_server()

    goal = XFeiTTSGoal()
    goal.xfei_tts_goal = speech_str
    tts_action_client.send_goal(goal)
    finished = tts_action_client.wait_for_result(timeout = rospy.Duration(10))# bool,取决于目标是否处理完成
    if finished:
        state = tts_action_client.get_state()   # int PENDING = 0 ACTIVE = 1 DONE = 2
        result = tts_action_client.get_result() # 返回result的名称和具体的值

        rospy.loginfo("Action finished, goal state: %i", state)
        rospy.loginfo("Action finished, xfei_tts_result: %s", result.xfei_tts_result) # 这里只输出结果值
    else:
        rospy.loginfo("Action did not finish before the time out.")

if __name__ == "__main__":
    try:
        text_to_speech("小福宝宝")
    except Exception:
        print "done"

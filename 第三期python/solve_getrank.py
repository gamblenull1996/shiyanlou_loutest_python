#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from pymongo import MongoClient

def get_rank(user_id):
    rank = 0
    client = MongoClient("localhost:27017")
    db = client.shiyanlou
    contests = db.contests

    group = {"$group": {
            	"_id": "$user_id",
                "score_sum": {"$sum": "$score"},
                "time_sum":  {"$sum": "$submit_time"}
        }
    }

    sort = {
	    "$sort":{
            "score_sum": -1,
            "time_sum": 1
        }
    }

    match = {
        "$match":{
            "_id": int(user_id)
        }
    }

    pipeline = [group, sort, match]
    result = contests.aggregate(pipeline)
    new_result = list(result)
    try:
        score = new_result[0]['score_sum']
        time = new_result[0]['time_sum']
    except:
        return 0


    # 首先是分数大于的 然后是分数相等但是时间比他少的
    # newrank = db.rank.find({ "$or": [ {"score_sum": {"$gt": score}}, {"score_sum": {"$eq": score}, "time_sum" :{"$lte": time}}] }).count()


    match = {
        "$match":{
            "$or": [
                {"score_sum": {"$gt": score}},
                {"score_sum": {"$gte": score}, "time_sum" :{"$lte": time}}
            ]
        }
    }


    # count = {
    #     "$count":" "
    # }
    #newpipeline = [group, match, count]
    newpipeline = [group, match]
    newrank = contests.aggregate(newpipeline)
    newrank = len(list(newrank))
    rank = newrank
    return rank

if len(sys.argv) != 2:
    print "Parameter error."
    sys.exit(1)

user_id = sys.argv[1]
rank = get_rank(user_id)

print user_id, rank


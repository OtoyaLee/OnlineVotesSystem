#添加候选人
def append_candidates():#candidate候选人
    vote_list=[]#储存候选人名
    while 1:
        candidate=input("输入命令或输入第%s位候选人名:"%(len(vote_list)+1)).strip()
        if candidate=="finish":#输入是finish命令时
            if len(vote_list)!=0:
                break
            else:
                print("请输入候选人名")
        elif candidate=="delete":#输入delete命令时
                vote_list.pop()#删除一个候选人名时
        elif len(candidate)==0:
            pass
        else:
            vote_list.append(candidate)
            print ("添加候选人名成功")
        candi_name=",".join(vote_list)
        print ("当前候选人名单为:%s"%candi_name)#
    return  vote_list


#添加投票
def append_vote(vote_list=[]):
    votes_name=[]#保存投票
    key_words_list=["stop","delete_last","clear","name"]#命令
    num_votes=0
    while 1:
        num_votes+=1
        voting=input("输入命令或投票给:").strip()#输入候选人名并进行投票
        if voting in key_words_list:
            print ("命令运行成功")
            if voting=="stop":
                break
            if voting=="delete_last":
                votes_name.pop()
            if voting=="clear":
                vote_name=[]
            if voting=="menu":
                print ("进入菜单")
        elif voting in [str(i) for i in range(1,len(vote_list)+1)]:#按顺序对应候选人名投票
            votes_name.append(vote_list[int(voting)-1])
            print ("投票%s成功"%vote_list[int(voting)-1])
        elif voting not in vote_list:
            name=",".join(vote_list)
            print ("请投票给%s其中一人%name")
        else:
            votes_name.append(voting)
            print ("投票%s成功"%voting)
        menu=input("是否继续投票(任意键:继续, stop:结束投票, help:查看命令, stats:查看当前统计信息):").strip()
        if menu=="stop":
            break
        if menu=="help":
            print ("内置命令")
            print ("1.stop: 输入stop结束投票")
            print ("2.delete_last:输入delete_last删除上一条投票")
            print ("3.clear:输入clear删除所有投票")
            print ("4.menu:回到菜单选择")
            print ("-------------------------------------")
        if menu=="stats":
            count=counter(votes_name)
            describe(count,temp=True)
    return  votes_name



#票数统计
def counter(votes_name):
    count_dict={}
    for i in votes_name:
        if i in count_dict:
            count_dict[i]+=1
        else:
            count_dict[i]=1
    return count_dict

def sort_by_value(votes,top_k=None):#votes参数是计数词典，top_k是输出前k个值
    items=votes.items()#取出字典中的items，每个items是一个key_value对
    backitems=[[v[1],v[0]] for v in items]
    backitems.sort(reverse=True)#排序
    if top_k:#如果要设置限制输出k个时
        return  backitems[:top_k]
    else:
        return  backitems


#describe()函数
def describe(votes, temp=False):
    sum_votes = sum([v for v in votes.values()])#求总票数
    if len(votes) == 0:#异常处理
        mean_votes = '没有投票，无法计算平均票数'
    else:
        mean_votes = sum_votes / len(votes)
        mean_votes = float('%.2f' % mean_votes)
    if temp is True:#设置标记，如果是临时输出，即使用命令stats输出时
        print('目前总票数为：%s' % str(sum_votes))
    else:
        print('总票数：%s' % str(sum_votes))
        print('平均票数：%s' % mean_votes)
    final = sort_by_value(votes, 10)
    for ind, i in enumerate(final):
        if temp is True:
            print('目前投票数第%s名是%s，票数为:%s，占总票数:%.2f%%' % (
            str(ind + 1), i[1], str(votes[i[1]]), 100 * i[0] / sum_votes))
        else:
            print('本次投票数第%s名是%s,票数为:%s,占总票数:%.2f%%' % (
            str(ind + 1), i[1], str(votes[i[1]]), 100 * i[0] / sum_votes))


#主运行模块
def online_voting():
    print("欢迎使用在线投票系统")
    print("使用规则介绍")
    print("1.启动在线投票系统后，会出现命令解释，这是在之后的投票过程中的一些命令")
    print("2.之后，系统会提醒您输入候选名单，例如本次投票的候选名单为(张三，李四)，我们需要一个一个按顺序输入其名字")
    print("3.输入完信息之后，需要按enter提交")
    print("在线投票系统已开启")
    print("---------------------------------")
    print("请输入本次投票的候选名单")
    print("如果发现候选人名填错，可以输入delete来删除上一个填入的候选人")
    vote_list=append_candidates()#运行添加候选人函数
    seq_vote_list=[str(i)+"."+vote_list[i-1] for i in range(1,len(vote_list)+1)]#打印出带序号的候选人名
    name=",".join(seq_vote_list)
    print("本次投票候选名单为 %s"%name)#打印最终候选人名
    print("请输入候选名单的内容，或者输入其序号，例如:输入1代表投票给候选名单第一位")
    print("---------------------------------")
    print("投票内置命令如下:")
    print("1.stop:输入stop结束投票")
    print("2.delete_last:输入delete_last删除上一条投票")
    print("3.clear:输入clear删除所有投票")
    print("4.menu:回到菜单选择")
    print("----------------------------------")
    votes=append_vote(vote_list=vote_list)#运行投票函数
    votes_count=counter(votes)#运行计数函数
    print("投票已结束")
    print("----------------------------------")
    print("输出统计信息:")
    describe(votes_count)#运行统计描述输出函数




online_voting()
# append_candidates()
# append_vote()
# counter()
# sort_by_value()
# describe()

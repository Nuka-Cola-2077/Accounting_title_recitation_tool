import random as r
##读取本地错题记录

try:
    错题统计={}
    f=open("store.csv","r",encoding="utf-8")
    f2=open("store2.csv","r",encoding="utf-8")
    q1=[]
    q2=[]
    w1=f.read()
    q1=w1.split("\n")
    q1.pop()

    w2=f2.read()
    q2=w2.split("\n")
    q2.pop()

    for i2 in range(len(q1)):
        错题统计[str(q1[i2])]=int(eval(q2[i2]))
    print(错题统计)
    print("本地错题记录读取成功\n\n")
except:
    错题统计={}
    print("未找到错题记录\n")
##会计科目，可以自行添加新的条目进去
资产类="库存现金,银行存款,其他货币资金,交易性金融资产,应收票据,应收账款,预付账款,应收股利,应收利息,其他应收款,坏账准备,代理业务资产,材料采购,在途物资,原材料,材料成本差异,库存商品,发出商品,商品进销差价,委托加工物资,周转材料,存货跌价准备,持有至到期投资,持有至到期投资减值准备,可供出售金融资产,长期股权投资,长期股权投资减值准备,投资性房地产,长期应收款,未实现融资收益,固定资产,累计折旧,固定资产减值准备,在建工程,工程物资,固定资产清理,无形资产,累计摊销,无形资产减值准备,商誉,长期待摊费用,递延所得税资产,待处理财产损溢"
负债类="短期借款,交易性金融负债,应付票据,应付账款,预收账款,应付职工薪酬,应交税费,应付利息,应付股利,其他应付款,代理业务负债,递延收益,长期借款,应付债券,长期应付款,未确认融资费用,专项应付款,预计负债,递延所得税负债"
所有者权益类="实收资本,资本公积, 其他综合收益,盈余公积,本年利润,利润分配,库存股"
成本类="生产成本,制造费用,劳务成本,研发支出"
损益类="主营业务收入,其他业务收入,公允价值变动损益,投资收益,其他收益,营业外收入,主营业务成本,其他业务成本,税金及附加,销售费用,管理费用,财务费用,资产减值损失,营业外支出,所得税费用,以前年度损益调整"
t1=资产类.split(",")
t2=负债类.split(",")
t3=所有者权益类.split(",")
t4=成本类.split(",")
t5=损益类.split(",")
d=["资产类","负债类","所有者权益类","成本类","损益类"]
错题=[]
##问答模块
times=eval(input("测试数量\n"))
num_of_correct=0
for i in range(times):
    ans=0
    group=0
    group=r.randint(1,5)#此变量为会计科目大类组编号
    group1="t"+str(group)#group1是选择会计科目的大类

    ordi=r.randint(0,len(eval(group1))-1)
    print("\n"+eval(group1)[ordi])
    try:
        ans=int(input("****属于哪一类****\n请输入编号 1资产类2负债类3所有者权益类4成本类5损益类\n"))
    except:
        print("输入错误")
        continue
    if group==ans:
        print("True")
        num_of_correct=num_of_correct+1
    else:
        print("False 正确答案是",end="")
        print(d[group-1])
        错题.append(eval(group1)[ordi])#把错题加入列表
    print("进度:%d/%d 正确率是：%.2f %%"%(i+1,times,round(num_of_correct/(i+1),4)*100))

##错题统计

for word in 错题:
    错题统计[word]=错题统计.get(word,0)+1
items=list(错题统计.items())

print("错题及错误次数：")
print(sorted(错题统计.items(),key=lambda x:x[1],reverse=True))


#保存错题记录到本地

f=open("store.csv","w",encoding="utf-8")
f2=open("store2.csv","w",encoding="utf-8")
for m,n in 错题统计.items():
    f.write(m+"\n")
    f2.write(str(n)+"\n")
f.close()
f2.close()
print("保存成功")
input("Press any key to quit")



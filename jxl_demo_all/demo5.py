# def   A():
#     a = 100
#     print(a)
#
# # print(A.a)
'''



class AiliPay():
    #具体产品角色
    def __init__(self,enable_yuebao=False):
        self.enable_yuebao = enable_yuebao

    def pay(self,money):
        if self.enable_yuebao:
            print('使用余额宝支付%s元'%money)
        else:
            print('使用支付宝支付%s元'%money)

class ApplePay():
    # 具体产品角色
    def pay(self,money):
        print('使用苹果支付支付%s元'%money)

class PaymentFactory:
    #工厂角色
    def create_payment(self,method):
        if method == 'alipay':
            return AiliPay()
        elif method == 'yuebao':
            return AiliPay(True)
        elif method == 'applepay':
            return ApplePay()
        else:
            return NameError

p = PaymentFactory()
f = p.create_payment('yuebao')
f.pay(100)
'''


# alist = [7,1,2,3,4,5]
# # alist.reverse()
# # alist.sort()
# blis = alist[::-1]
# print(blis)
#
# print(alist)

def quick_sort(qlist):
    if qlist == []:
        return []
    else:
        qfirst = qlist[0]
        qless = quick_sort([l for l in qlist[1:] if l < qfirst])
        qmore = quick_sort([m for m in qlist[1:] if m >= qfirst])
        return qless + [qfirst] + qmore

qlist = quick_sort([4,5,6,7,3,2,6,9,8])
print(qlist)



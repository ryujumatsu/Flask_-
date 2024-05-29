def calcsalary(gal):
    #給料の入力
    salary=float(gal) 
    #税率・基準額の設定
    base_tax_rate=0.1 
    over_tax_rate=0.2 
    base_amount=1000000
    #給与に応じた税額・手取り額の計算
    if(salary>base_amount):
        #100万を超える場合
        base_tax_amount=base_amount*base_tax_rate
        over_tax_amount=(salary-base_amount)*over_tax_rate
        tax_amount=base_tax_amount+over_tax_amount
        pay_amount=salary-tax_amount
    else:
        #100万以下の場合
        tax_amount=salary*base_tax_rate
        pay_amount=salary-tax_amount

    #税額・支給額の四捨五入
    round_tax=str(int(round(tax_amount)))
    round_pay=str(int(round(pay_amount)))
    #税額・支給額の出力
    return(round_pay,round_tax)
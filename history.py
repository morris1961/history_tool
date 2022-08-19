h = '''註腳程式說明：\n
1.  解壓縮後執行
2.  輸入方式按程式內之說明，每打完一個註腳後，程式即會自動儲存。
3.  儲存的註腳會存在資料夾中程式下方的記事本(output.txt)。
4.  僅需輸入會變的資訊（如作者名、出版地等），其餘標點符號（如：、《》等），程式會自動排完。\n'''
print(h)
while (True):
    with open("output.txt", "a", encoding='utf-8' ) as f:
        mode1 = input("\n請輸入使用方式\n0.退出\n1.註腳\n2.參考書目\nh.幫助\n輸入數字即可:")
        p = ""
        if mode1 == "h":#幫助
            print(h)
            continue
        elif mode1 == "0":#退出
            break
        elif mode1 == "1":#註腳
            book = input("\n請輸入書類\n0.退回上一層\n1.專書\n2.譯著\n3.書中篇章\n4.專書論文\n5.期刊論文\n6.書評\n7.學位論文\n8.史料\n9.檔案\n10.報紙\n11.網頁\n輸入數字即可:")
            if book == "0":#退回上一層
                continue
            check_16 = int(book)
            if (check_16 <= 6 and check_16 >= 1):
                mode2 = input("\n請輸入首次或二次以上\n0.退回上一層\n1.首次\n2.二次以上\n輸入數字即可:")
                if mode2 == "0":#退回上一層
                    continue
                if mode2 == "1":#首次
                    if book == "1":#專書
                        title = input("請輸入題名\n:")
                        author = input("請輸入作者（作者A、作者B）\n:")
                        trans = input("請輸入譯者(若無請直接enter跳過)（譯者A、譯者B）\n:")
                        editor = input("請輸入編者(若無請直接enter跳過)（編者A、編者B）\n:")
                        publish = input("請輸入出版（出版地：出版社）\n:")
                        date = input("請輸入出版日期（西元年）\n:")
                        page = input("請輸入頁數（頁碼-頁碼）\n:")
                        if trans == "" and editor == "":
                            p += author + "，《" + title + "》（" + publish + "，" + date + "），頁" + page + "。"
                        else:
                            p += author + "撰"
                            if trans != "":
                                p += "，" + trans + "譯"
                            if editor != "":
                                p += "（" + editor + "）"
                            p += "，《" + title + "》（" + publish + "，" + date + "），頁" + page + "。"
                    elif book == "2":#譯著
                        title = input("請輸入題名\n:")
                        author = input("請輸入作者（作者A、作者B）\n:")
                        trans = input("請輸入譯者(若無請直接enter跳過)（譯者A、譯者B）\n:")
                        publish = input("請輸入出版（出版地：出版社）\n:")
                        date = input("請輸入出版日期（西元年）\n:")
                        page = input("請輸入頁數（頁碼-頁碼）\n:")
                        if(author.find("、") != -1):
                            p += author[0:author.find("、")] + "等著，"
                        else:
                            p += author + "著，"
                        if(trans.find("、") != -1):
                            p += trans[0:trans.find("、")] + "等"
                        else:
                            p += trans
                        p += "譯，"
                        p += "《" + title + "》（" + publish + "，" + date + "），頁" + page + "。"   
                    elif book == "3":#書中篇章
                        title = input("請輸入題名\n:")
                        para = input("請輸入篇名（第一章 世界史）\n:")
                        authorUnique = input("請輸入篇章作者(若無請直接enter跳過)（篇章作者A、篇章作者B）\n:")
                        author = input("請輸入作者（作者A、作者B）\n:")
                        trans = input("請輸入譯者(若無請直接enter跳過)（譯者A、譯者B）\n:")
                        publish = input("請輸入出版（出版地：出版社）\n:")
                        date = input("請輸入出版日期（西元年）\n:")
                        page = input("請輸入頁數（頁碼-頁碼）\n:")
                        istrans = 0
                        if(trans != ""):
                            istrans = 1
                        if(authorUnique != ""):
                            p += authorUnique
                            p += "，〈" + para[para.find(" ")+1:len(para)] + "〉，"
                            if(author.find("、") != -1):
                                p += author[0:author.find("、")] + "等著"
                            else:
                                p += author
                                if(istrans):
                                    p += "著"
                            p += "，"
                            if(trans != ""):
                                if(trans.find("、") != -1):
                                    p += trans[0:trans.find("、")] + "等"
                                else:
                                    p += trans
                                p += "譯，"
                            p += "《" + title + "》（" + publish + "，" + date + "），" + para[0:para.find(" ")] +"，頁" + page + "。"
                        else:
                            if(author.find("、") != -1):
                                p += author[0:author.find("、")] + "等著"
                            else:
                                p += author
                                if(istrans):
                                    p += "著"
                            p += "，"
                            if(trans.find("、") != -1):
                                p += trans[0:trans.find("、")] + "等"
                            else:
                                p += trans
                            p += "譯，"
                            p += "《" + title + "》（" + publish + "，" + date + "），" + para[0:para.find(" ")] + "〈" + para[para.find(" ")+1:len(para)] + "〉頁" + page + "。"
                    elif book == "4":#專書論文
                        title = input("請輸入題名\n:")
                        para = input("請輸入篇名（第一章 世界史）\n:")
                        author = input("請輸入作者（作者A、作者B）\n:")
                        trans = input("請輸入譯者(若無請直接enter跳過)（譯者A、譯者B）\n:")
                        publish = input("請輸入出版（出版地：出版社）\n:")
                        date = input("請輸入出版日期（西元年）\n:")
                        page = input("請輸入頁數（頁碼-頁碼）\n:")
                        family = input("請輸入是否收入氏著（是 or 否）\n:")
                        if family == "否":
                            editor = input("請輸入編者（編者A、編者B）\n:")
                        if(author.find("、") != -1):
                            p += author[0:author.find("、")] + "等"
                        else:
                            p += author
                        p += "，"
                        if(trans != ""):
                            if(trans.find("、") != -1):
                                p += trans[0:trans.find("、")] + "等"
                            else:
                                p += trans
                            p += "譯，"
                        p += "〈" + para + "〉"
                        if family == "是":
                            p += "收入氏著" + "，《" + title + "》（" + publish + "，" + date + "），頁" + page + "。"
                        elif family == "否":
                            p += "編，" + editor + "，《" + title + "》（" + publish + "，" + date + "），頁" + page + "。"
                    elif book == "5":#期刊論文
                        title = input("請輸入題名\n:")
                        author = input("請輸入作者（作者A、作者B）\n:")
                        trans = input("請輸入譯者(若無請直接enter跳過)（譯者A、譯者B）\n:")
                        jour = input("請輸入期刊名\n:")
                        jourDate = input("請輸入卷期（第12卷第2期）\n:")
                        date = input("請輸入出版日期（2000年12月）\n:")
                        publish = input("請輸入出版地點（臺北）\n:")
                        page = input("請輸入頁數（頁碼-頁碼）\n:")
                        istrans = 0
                        if(trans != ""):
                            istrans = 1
                        if(author.find("、") != -1):
                            p += author[0:author.find("、")] + "等"
                        else:
                            p += author
                        if (istrans):
                            p += "著，"
                        else:
                            p += "，"
                        if(trans != ""):
                            if(trans.find("、") != -1):
                                p += trans[0:trans.find("、")] + "等"
                            else:
                                p += trans
                            p += "譯，"
                        if(jourDate.find("年") == -1 ):
                            p += "〈" + title + "〉" + "，《" + jour + "》" + jourDate + "（" + date + "，" + publish + "），頁" + page + "。"
                        else:
                            p += "〈" + title + "〉" + "，《" + jour + "》" + jourDate + "，頁" + page + "。"
                    elif book == "6":#書評
                        title = input("請輸入題名\n:")
                        author = input("請輸入作者（作者A、作者B）\n:")
                        trans = input("請輸入譯者(若無請直接enter跳過)（譯者A、譯者B）\n:")
                        jour = input("請輸入期刊名\n:")
                        jourDate = input("請輸入卷期（第12卷第2期）\n:")
                        publish = input("請輸入出版（出版地：出版社）\n:")
                        date = input("請輸入出版日期（西元年）\n:")
                        page = input("請輸入頁數（頁碼-頁碼）\n:")
                        if(author.find("、") != -1):
                            p += author[0:author.find("、")] + "等"
                        else:
                            p += author 
                        p += "，"
                        if(trans != ""):
                            if(trans.find("、") != -1):
                                p += trans[0:trans.find("、")] + "等"
                            else:
                                p += trans
                            p += "譯，"
                        p += "〈" + title + "〉" + "，《" + jour + "》" + jourDate + "（" + date + "，" + publish + "），頁" + page + "。"
                elif mode2 == "2":#二次或以上
                    if book == "1":#專書
                        title = input("請輸入題名\n:")
                        author = input("請輸入作者（作者A、作者B）\n:")
                        page = input("請輸入頁數（頁碼-頁碼）\n:")
                        p += author + "，《" + title + "》，頁" + page + "。"
                    elif book == "2":#譯著
                        title = input("請輸入題名\n:")
                        author = input("請輸入作者（作者A、作者B）\n:")
                        trans = input("請輸入譯者(若無請直接enter跳過)（譯者A、譯者B）\n:")
                        page = input("請輸入頁數（頁碼-頁碼）\n:")
                        p += author + "，" + trans + "，《" + title + "》，頁" + page + "。"
                    elif book == "3":#書中篇章
                        title = input("請輸入題名\n:")
                        para = input("請輸入篇名（第一章 世界史）\n:")
                        authorUnique = input("請輸入篇章作者(若無請直接enter跳過)（篇章作者A、篇章作者B）\n:")
                        author = input("請輸入作者（作者A、作者B）\n:")
                        page = input("請輸入頁數（頁碼-頁碼）\n:")
                        if(authorUnique != ""):
                            p += authorUnique
                            p += "，〈" + para[para.find(" ")+1:len(para)] + "〉，"
                            p += "頁" + page + "。"
                        else:
                            if(author.find("、") != -1):
                                p += author[0:author.find("、")] + "等"
                            else:
                                p += author 
                            p += "著，"
                            p += "《" + title + "》，" + "〈" + para[para.find(" ")+1:len(para)] + "〉頁" + page + "。"
                    elif book == "4":#專書論文
                        title = input("請輸入題名\n:")
                        author = input("請輸入作者（作者A、作者B）\n:")
                        page = input("請輸入頁數（頁碼-頁碼）\n:")
                        family = input("請輸入是否收入氏著（是 or 否）\n:")
                        if(author.find("、") != -1):
                            p += author[0:author.find("、")] + "等"
                        else:
                            p += author 
                        p += "，"
                        p += "〈" + para + "〉"
                        if family == "是":
                            p += "收入氏著" + "，頁" + page + "。"
                        elif family == "否":
                            p += "，頁" + page + "。"
                    elif book == "5":#期刊論文
                        title = input("請輸入題名\n:")
                        author = input("請輸入作者（作者A、作者B）\n:")
                        page = input("請輸入頁數（頁碼-頁碼）\n:")
                        if(author.find("、") != -1):
                            p += author[0:author.find("、")] + "等"
                        else:
                            p += author 
                        p += "著，"
                        p += "〈" + title + "〉，頁" + page + "。"
                    elif book == "6":#書評
                        title = input("請輸入題名\n:")
                        author = input("請輸入作者（作者A、作者B）\n:")
                        page = input("請輸入頁數（頁碼-頁碼）\n:")
                        p = ""
                        if(author.find("、") != -1):
                            p += author[0:author.find("、")] + "等"
                        else:
                            p += author 
                        p += "著，"
                        p += "〈" + title + "〉，頁" + page + "。"
                else:
                    print("輸入錯誤！")
                    continue
            else:
                if book == "7":#學位論文
                    title = input("請輸入論文名稱\n:")
                    author = input("請輸入作者（作者A、作者B）\n:")
                    publish = input("請輸入來源（地點：學校系所碩/博士論文）\n:")
                    date = input("請輸入畢業年份（畢業年份）\n:")
                    page = input("請輸入頁數（頁碼-頁碼）\n:")
                    p += author + "，〈" + title + "〉（" + publish + "，" + date + "），頁" + page + "。"
                elif book == "8":#史料
                    title = input("請輸入書名\n:")
                    author = input("請輸入作者（作者A、作者B）\n:")
                    together = input("請輸入叢書名(若無請直接enter跳過)（叢書名）\n:")
                    num = input("請輸入冊數（冊數）\n:")
                    publish = input("請輸入來源（出版地：出版社）\n:")
                    date = input("請輸入出版年（出版年）\n:")
                    ver = input("請輸入版本（版本）\n:")
                    rol = input("請輸入卷數（卷數）\n:")
                    para = input("請輸入篇名（篇名）\n:")
                    page = input("請輸入頁數（頁碼-頁碼）\n:")
                    p += author + "，《" + title + "》"
                    if together != "":
                        p += "，收入《" + together + "》"
                    p += num + "（" + publish + "，" + date + "，" + ver + "）" + rol + "，" + "〈" + para + "〉" + "，頁" + page + "。"
                elif book == "9":#檔案
                    title = input("請輸入檔案名稱\n:")
                    publish = input("請輸入館藏地\n:")
                    page = input("請輸入檔案編號\n:")
                    p += title + "，" + publish + "，" + page + "。"
                elif book == "10":#報紙
                    title = input("請輸入報紙名稱\n:")
                    para = input("請輸入標題\n:")
                    author = input("請輸入作者(若無請直接enter跳過)（作者A、作者B）\n:")
                    publish = input("請輸入出版地\n:")
                    date = input("請輸入時間（年月日）\n:")
                    page = input("請輸入版頁\n:")
                    if author != "":
                        p += author + "，"
                    p += "〈" + para + "〉，《" + title + "》（" + publish + "）" + "，" + date + "，" + page + "。"
                elif book == "11":#網頁
                    title = input("請輸入網站名稱\n:")
                    para = input("請輸入網址\n:")
                    date = input("請輸入檢索時間（x年x月x日）\n:")
                    p += title + "，" + para + "，（檢索日期：" + date + "）。"
                else:
                    print("輸入錯誤！")
                    continue
        elif mode1 == "2":#參考書目
            book = input("請輸入書類\n1.專書\n2.譯著\n3.專書論文\n4.期刊論文\n輸入數字即可:")
            if book == "1":#專書
                title = input("請輸入題名\n:")
                author = input("請輸入作者（作者A、作者B）\n:")
                publish = input("請輸入出版（出版地：出版社）\n:")
                date = input("請輸入出版日期（西元年）\n:")
                p += author + "，《" + title + "》。" + publish + "，" + date + "。"
            elif book == "2":#譯著
                title = input("請輸入題名\n:")
                author = input("請輸入作者（作者A、作者B）\n:")
                trans = input("請輸入譯者(若無請直接enter跳過)（譯者A、譯者B）\n:")
                publish = input("請輸入出版（出版地：出版社）\n:")
                date = input("請輸入出版日期（西元年）\n:")
                p += author
                p += "著，"
                p += trans
                p += "譯"
                p += "，《" + title + "》。" + publish + "，" + date + "。"   
            elif book == "3":#專書論文
                title = input("請輸入題名\n:")
                para = input("請輸入篇名（第一章 世界史）\n:")
                author = input("請輸入作者（作者A、作者B）\n:")
                trans = input("請輸入譯者(若無請直接enter跳過)（譯者A、譯者B）\n:")
                page = input("請輸入頁數（頁碼-頁碼）\n:")
                publish = input("請輸入出版（出版地：出版社）\n:")
                date = input("請輸入出版日期（西元年）\n:")
                istrans = 0
                if(trans != ""):
                    istrans = 1
                if(author.find("、") != -1):
                    p += author[0:author.find("、")] + "等"
                else:
                    p += author 
                if(istrans):
                    p += "著，"
                else:
                    p += "，"
                if(istrans):
                    if(trans.find("、") != -1):
                        p += trans[0:trans.find("、")] + "等"
                    else:
                        p += trans
                    p += "譯，"
                p += "〈" + para + "〉"
                p += "，《" + title + "》，頁" + page + "。" + publish + "，" + date + "。"
            elif book == "4":#期刊論文
                title = input("請輸入題名\n:")
                author = input("請輸入作者（作者A、作者B）\n:")
                trans = input("請輸入譯者(若無請直接enter跳過)（譯者A、譯者B）\n:")
                jour = input("請輸入期刊名\n:")
                jourDate = input("請輸入卷期（第12卷第2期）\n:")
                date = input("請輸入出版日期（2000年12月）\n:")
                publish = input("請輸入出版地點（臺北）\n:")
                page = input("請輸入頁數（頁碼-頁碼）\n:")
                istrans = 0
                if(trans != ""):
                    istrans = 1
                if(author.find("、") != -1):
                    p += author[0:author.find("、")] + "等"
                else:
                    p += author 
                if(istrans):
                    p += "著，"
                else:
                    p += "，"
                if(istrans):
                    if(trans.find("、") != -1):
                        p += trans[0:trans.find("、")] + "等"
                    else:
                        p += trans
                    p += "譯，"
                if(jourDate.find("年") == -1 ):
                    p += "〈" + title + "〉" + "，《" + jour + "》" + jourDate + "，" + date + "，" + publish + "，頁" + page + "。"
                else:
                    p += "〈" + title + "〉" + "，《" + jour + "》" + jourDate + "，頁" + page + "。"
            else:
                print("輸入錯誤！")
                continue
        else:
            print("輸入錯誤！")
            continue
        print("----------------------\n",p,"\n----------------------")
        if(f.write(p+"\n")):
            print("儲存成功！")
        else:
            print("儲存失敗！")
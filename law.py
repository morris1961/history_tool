h = '''註解程式說明：\n
1.  解壓縮後執行
2.  輸入方式按程式內之說明，每打完一個註解後，程式即會自動儲存。
3.  儲存的註解會存在資料夾中程式下方的記事本(output.txt)。
4.  僅需輸入會變的資訊（如作者名、出版地等），其餘標點符號（如：、《》等），程式會自動排完。\n'''
print(h)
while (True):
    mode1 = input("\n請輸入使用方式\n0.退出\n1.註解\n2.參考文獻\nh.幫助\n輸入數字即可:")
    p = ""
    if mode1 == "h":#幫助
        print(h)
        continue
    elif mode1 == "0":#退出
        break
    elif mode1 == "1":#註解
        book = input("\n請輸入書類\n0.退回上一層\n1.一般書籍或論文\n2.政府公報\n3.報紙\n4.投書\n5.網頁\n6.立法院關係文書\n輸入數字即可:")
        if book == "0":#退回上一層
            continue
        elif book == "1": #一般書籍或論文
            author = input("請輸入作者（作者A、作者B）\n:")
            p += author

            trans = input("請輸入譯者（若無請直接enter跳過）（譯者A、譯者B）\n:")
            if trans != "":
                p += f"（著），{trans}（譯）"

            date = input("請輸入出版日期（西元年）\n:")
            p += f"（{date}），"

            para_main_title = input("請輸入篇名主標題（若無請直接enter跳過）\n:")
            if para_main_title != "":
                p += f"〈{para_main_title}"
                para_sub_title= input("請輸入篇名副標題（若無請直接enter跳過）\n:")
                if para_sub_title != "":
                    p += f"：{para_sub_title}"
                p += "〉，"
            
            editor = input("請輸入編者（若無請直接enter跳過）（編者A、編者B）\n:")
            if editor != "":
                p += f"{editor}（編），"

            book_main_title = input("請輸入書名主標題（若無請直接enter跳過）\n:")
            if book_main_title != "":
                p += f"《{book_main_title}"
                book_sub_title= input("請輸入書名副標題（若無請直接enter跳過）\n:")
                if book_sub_title != "":
                    p += f"：{book_sub_title}"
                p += "》，"

            edition = input("請輸入版次（若無請直接enter跳過）\n:")
            if edition != "":
                p += f"{edition}，"

            page = input("請輸入頁數（頁碼-頁碼）\n:")
            p += f"頁 {page}，"

            publish = input("請輸入出版社\n:")
            p += f"{publish}。"
        elif book == "2": #政府公報
            place = input("請輸入公報處\n:")
            date = input("請輸入出版日期（西元年）\n:")
            book_main_title = input("請輸入書名\n:")
            vol = input("請輸入第幾卷（阿拉伯數字）\n:")
            issue = input("請輸入第幾期（阿拉伯數字）\n:")
            p += f"{place}（{date}），《{book_main_title}》，{vol} 卷 {issue} 期，"

            book = input("請輸入冊（若無請直接enter跳過）\n:")
            if book != "":
                p += f"{book}冊，"
                
            page = input("請輸入頁數（頁碼-頁碼）\n:")
            p += f"頁 {page}，"

            publish = input("請輸入出版社\n:")
            p += f"{publish}。"
        elif book == "3": #報紙
            place = input("請輸入出版社\n:")
            date = input("請輸入出版日期（月/日/西元年）\n:")
            book_main_title = input("請輸入標題\n:")
            edition = input("請輸入版次或網址\n:")
            p += f"{place}（{date}），〈{book_main_title}〉，{edition}"
            final = input("請輸入最後瀏覽日（若無請直接enter跳過）（月/日/西元年）\n:")
            if final != "":
                p += f"（{final}）"
            p += "。"
        elif book == "4": #投書
            author = input("請輸入作者（作者A、作者B）\n:")
            date = input("請輸入出版日期（月/日/西元年）\n:")
            p += f"{author}（{date}），"

            para_main_title = input("請輸入篇名主標題（若無請直接enter跳過）\n:")
            if para_main_title != "":
                p += f"〈{para_main_title}"
                para_sub_title= input("請輸入篇名副標題（若無請直接enter跳過）\n:")
                if para_sub_title != "":
                    p += f"：{para_sub_title}"
                p += "〉，"

            book_main_title = input("請輸入書名主標題（若無請直接enter跳過）\n:")
            if book_main_title != "":
                p += f"《{book_main_title}"
                book_sub_title= input("請輸入書名副標題（若無請直接enter跳過）\n:")
                if book_sub_title != "":
                    p += f"：{book_sub_title}"
                p += "》，"

            edition = input("請輸入版次或網址\n:")
            p += edition

            final = input("請輸入最後瀏覽日（若無請直接enter跳過）（月/日/西元年）\n:")
            if final != "":
                p += f"（{final}）"
            p += "。"
        elif book == "5": #網頁
            place = input("請輸入網站名稱\n:")
            edition = input("請輸入版次或網址\n:")
            final = input("請輸入最後瀏覽日（月/日/西元年）\n:")
            p += f"{place}，{edition}（{final}）。"
        elif book == "6": #立法院關係文書
            date = input("請輸入出版日期（西元年）\n:")
            book_main_title = input("請輸入書名主標題（若無請直接enter跳過）\n:")
            page = input("請輸入頁數（頁碼-頁碼）\n:")
            p += f"立法院議案關係文書（{date}），《{book_main_title}》，頁政 {page}，"

            edition = input("請輸入版次或網址\n:")
            p += edition

            final = input("請輸入最後瀏覽日（若無請直接enter跳過）（月/日/西元年）\n:")
            if final != "":
                p += f"（{final}）"
            p += "。"
        else:
            print("輸入錯誤！")
            continue
    elif mode1 == "2": #參考文獻
        book = input("請輸入書類\n1.一般書籍\n2.翻譯書籍\n3.書之篇章\n4.期刊論文\n輸入數字即可:")
        if book == "1": #一般書籍
            author = input("請輸入作者（如果是有數量龐大的作者群，如 10 位以上，則只列出第一作者姓名並加上等）（若無請直接enter跳過）（作者A、作者B）\n:")
            if author != "":
                p += author
                if author.find("等") != -1:
                    p += "（等著）"
                
            editor = input("請輸入編者（如果是有數量龐大的作者群，如 10 位以上，則只列出第一編者姓名並加上等）（若無請直接enter跳過）（編者A、編者B）\n:")
            if editor != "":
                p += f"{editor}（"
                if author.find("等") != -1:
                    p += "等"
                p += "編）"

            date = input("請輸入出版日期（西元年）\n:")
            p += f"（{date}），"

            book_main_title = input("請輸入書名主標題\n:")
            p += f"《{book_main_title}"
            book_sub_title= input("請輸入書名副標題（若無請直接enter跳過）\n:")
            if book_sub_title != "":
                p += f"：{book_sub_title}"
            p += "》，"

            edition = input("請輸入版次（若無請直接enter跳過）\n:")
            if edition != "":
                p += f"{edition}，"

            publish = input("請輸入出版社\n:")
            p += f"{publish}。"
        elif book == "2": #翻譯書籍
            author = input("請輸入作者（作者A、作者B）\n:")
            trans = input("請輸入編者（譯者A、譯者B）\n:")
            date = input("請輸入出版日期（西元年）\n:")
            p += f"{author}（著），{trans}（譯）（{date}），"

            book_main_title = input("請輸入書名主標題\n:")
            p += f"《{book_main_title}"
            book_sub_title= input("請輸入書名副標題（若無請直接enter跳過）\n:")
            if book_sub_title != "":
                p += f"：{book_sub_title}"
            p += "》，"

            edition = input("請輸入版次（若無請直接enter跳過）\n:")
            if edition != "":
                p += f"{edition}，"

            publish = input("請輸入出版社\n:")
            p += publish

            simplified = input("請輸入是否為簡體字版（是／否）\n:")
            if simplified == "是":
                p += "（簡體字版）"

            p += "。"
        elif book == "3": #書之篇章
            author = input("請輸入作者（作者A、作者B）\n:")
            p += author

            trans = input("請輸入譯者（若無請直接enter跳過）（譯者A、譯者B）\n:")
            if trans != "":
                p += f"（著），{trans}（譯）"

            date = input("請輸入出版日期（西元年）\n:")
            p += f"（{date}），"

            para_main_title = input("請輸入篇名主標題\n:")
            p += f"〈{para_main_title}"
            para_sub_title= input("請輸入篇名副標題（若無請直接enter跳過）\n:")
            if para_sub_title != "":
                p += f"：{para_sub_title}"
            p += "〉，"
            
            editor = input("請輸入編者（編者A、編者B）\n:")
            if editor != "":
                p += f"收於：編者{editor}（編），"

            book_main_title = input("請輸入書名主標題\n:")
            p += f"《{book_main_title}"
            book_sub_title= input("請輸入書名副標題（若無請直接enter跳過）\n:")
            if book_sub_title != "":
                p += f"：{book_sub_title}"
            p += "》，"

            edition = input("請輸入版次（若無請直接enter跳過）\n:")
            if edition != "":
                p += f"{edition}，"

            page = input("請輸入頁數（頁碼-頁碼）\n:")
            p += f"頁 {page}，"

            publish = input("請輸入出版社\n:")
            p += publish

            simplified = input("請輸入是否為簡體字版（是／否）\n:")
            if simplified == "是":
                p += "（簡體字版）"

            p += "。"
        elif book == "4": #期刊論文
            author = input("請輸入作者（作者A、作者B）\n:")
            date = input("請輸入出版日期（西元年）\n:")
            p += f"{author}（{date}），"

            para_main_title = input("請輸入期刊名主標題\n:")
            p += f"〈{para_main_title}"
            para_sub_title= input("請輸入期刊名副標題（若無請直接enter跳過）\n:")
            if para_sub_title != "":
                p += f"：{para_sub_title}"
            p += "〉，"

            vol = input("請輸入第幾卷（阿拉伯數字）\n:")
            issue = input("請輸入第幾期（阿拉伯數字）\n:")
            p += f"{vol} 卷 {issue} 期"

            special = input("請輸入是否是特刊（是／否）\n:")
            if special != "":
                p += "特刊"
            p += "，"

            page = input("請輸入頁數（頁碼-頁碼）\n:")
            p += f"頁 {page}。"
        elif book == "5": #研討會論文
            author = input("請輸入作者（作者A、作者B）\n:")
            date = input("請輸入出版日期（xxxx 年 xx 月）\n:")
            p += f"{author}（{date}），"

            para_main_title = input("請輸入文章主標題\n:")
            p += f"〈{para_main_title}"
            para_sub_title= input("請輸入文章副標題（若無請直接enter跳過）\n:")
            if para_sub_title != "":
                p += f"：{para_sub_title}"
            p += "〉，"

            name = input("請輸入研討會名稱\n:")
            publish = input("請輸入舉辦單位（單位A、單位B）\n:")
            place = input("請輸入舉辦地\n:")
            p += f"發表於：《{name}》，{publish}（主辦），{place}。"
        elif book == "6": #未出版之學位論文
            author = input("請輸入作者（作者A、作者B）\n:")
            date = input("請輸入出版日期（西元年）\n:")
            title = input("請輸入論文名稱\n:")
            depart = input("請輸入學校及系所名稱學位（國立臺灣大學法律學研究所碩士）\n:")
            place = input("請輸入學校所在地\n:")
            p += f"{author}（{date}），《{title}》，{depart}論文（未出版），{place}。"
        elif book == "7": #電子書或網路單篇文章
            author = input("請輸入作者（作者A、作者B）\n:")
            date = input("請輸入出版日期（西元年）\n:")
            title = input("請輸入文章標題\n:")
            domain = input("請輸入網址\n:")
            p += f"{author}（{date}），《{title}》，載於：{domain}。"
        elif book == "8": #網路期刊文章
            author = input("請輸入作者（作者A、作者B）\n:")
            date = input("請輸入出版日期（西元年）\n:")
            title = input("請輸入文章標題\n:")
            jour_title = input("請輸入期刊名\n:")
            p += f"{author}（{date}），〈{title}〉，《{jour_title}》，"

            vol = input("請輸入第幾卷（阿拉伯數字）\n:")
            if vol != "":
                p += f"{vol} 卷 "

            issue = input("請輸入第幾期（阿拉伯數字）\n:")
            domain = input("請輸入網址\n:")
            p += f"{issue} 期，載於：{domain}。"
        else:
            print("輸入錯誤！")
            continue
    else:
        print("輸入錯誤！")
        continue
    print("----------------------\n",p,"\n----------------------")
    with open("output.txt", "a", encoding='utf-8' ) as f:
        if(f.write(p+"\n")):
            print("儲存成功！")
        else:
            print("儲存失敗！")
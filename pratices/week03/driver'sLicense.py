correctAnswer = {
    1: "A", 2: "C", 3: "A", 4: "A", 5: "D",
    6: "B", 7: "C", 8: "A", 9: "C", 10: "B",
    11: "A", 12: "D", 13: "C", 14: "A", 15: "D",
    16: "C", 17: "B", 18: "B", 19: "D", 20: "A"
}
testDict = [
    {
        "ques": "Khái niệm “phương tiện giao thông thô sơ đường bộ” được hiểu thế nào là đúng?",
        "options": [
            "A: Gồm xe đạp (kể cả xe đạp máy, xe đạp điện), xe xích lô, xe lăn dùng cho người khuyết tật, xe súc vật kéo và các loại xe tương tự.",
            "B: Gồm xe đạp (kể cả xe đạp máy, xe đạp điện), xe gắn máy, xe cơ giới dùng cho người khuyết tật và xe máy chuyên dùng.",
            "C: Gồm xe ô tô, máy kéo, rơ moóc hoặc sơ mi rơ moóc được kéo bởi xe ô tô, máy kéo."
     ]
    },
    {
        "ques": "“Phương tiện tham gia giao thông đường bộ” gồm những loại nào?",
        "options": [
            "A: Phương tiện giao thông cơ giới đường bộ.",
            "B: Phương tiện giao thông thô sơ đường bộ và xe máy chuyên dùng.",
            "C: Cả ý 1 và ý 2."
        ]
    },
    {
        "ques": "“Trên đường có nhiều làn đường cho xe đi cùng chiều được phân biệt bằng vạch kẻ phân làn đường, người điều khiển phương tiện phải cho xe đi như thế nào?",
        "options": [
            "A: Cho xe đi trên bất kỳ làn đường nào hoặc giữa 02 làn đường nếu không có xe phía trước; khi cần thiết phải chuyển làn đường, người lái xe phải quan sát xe phía trước để bảo đảm an toàn.",
            "B: Phải cho xe đi trong một làn đường và chỉ được chuyển làn đường ở những nơi cho phép; khi chuyển làn phải có tín hiệu báo trước và phải bảo đảm an toàn.",
            "C: Phải cho xe đi trong một làn đường, khi cần thiết phải chuyển làn đường, người lái xe phải quan sát xe phía trước để bảo đảm an toàn."
        ]
    },
    {
        "ques": "Khi tránh xe đi ngược chiều, các xe phải nhường đường như thế nào là đúng quy tắc giao thông?",
        "options": [
            "A: Xe xuống dốc phải nhường đường cho xe đang lên dốc; xe nào có chướng ngại vật phía trước phải nhường đường cho xe không có chướng ngại vật đi trước.",
            "B: Nơi đường hẹp chỉ đủ cho một xe chạy và có chỗ tránh xe thì xe nào ở gần chỗ tránh hơn phải vào vị trí tránh, nhường đường cho xe kia đi.",
            "C: Xe lên dốc phải nhường đường cho xe xuống dốc; xe nào không có chướng ngại vật phía trước phải nhường đường cho xe có chướng ngại vật đi trước",
            "D: Cả ý 1 và ý 2."
        ]
    },
    {
        "ques": "Tại nơi đường bộ giao nhau cùng mức với đường sắt chỉ có đèn tín hiệu hoặc chuông báo hiệu, khi đèn tín hiệu màu đỏ đã bật sáng hoặc có tiếng chuông báo hiệu, người tham gia giao thông phải dừng lại ngay và giữ khoảng cách tối thiểu bao nhiêu mét tính từ ray gần nhất?",
        "options": [
            "A: 5m",
            "B: 3m",
            "C: 4m"
        ]
    },
    {
        "ques": "Người điều khiển phương tiện tham gia giao thông trong hầm đường bộ ngoài việc phải tuân thủ các quy tắc giao thông còn phải thực hiện những quy định nào dưới đây?",
        "options": [
            "A: Xe cơ giới, xe máy chuyên dùng phải bật đèn; xe thô sơ phải bật đèn hoặc có vật phát sáng báo hiệu; chỉ được dừng xe, đỗ xe ở nơi quy định.",
            "B: Xe cơ giới phải bật đèn ngay cả khi đường hầm sáng; phải cho xe chạy trên một làn đường và chỉ chuyển làn ở nơi được phép; được quay đầu xe, lùi xe khi cần thiết.",
            "C: Xe máy chuyên dùng phải bật đèn ngay cả khi đường hầm sáng; phải cho xe chạy trên một làn đường và chỉ chuyển làn ở nơi được phép; được quay đầu xe, lùi xe khi cần thiết."
        ]
    }
]

def formatTest():
        for i in range(len(testDict)):
            print('Question ',i + 1, ": ", testDict[i]['ques'])

            #print options
            for j in range(len(testDict[i]['options'])):
                print(testDict[i]['options'][j])

#driver_lisence()

def main():
    list = ["A", "B", "C", "D"]
    formatTest()
    quesNumber = 1
    score = 0
    while(quesNumber <= 6):
        userAnswer = input("Question " + str(quesNumber) + ": ")
        check = userAnswer.islower()

        if check or userAnswer not in list:
            print("Invalid input")
            quesNumber -= 1
            continue


        if (correctAnswer.get(quesNumber) == userAnswer):
            score = score + 1
        quesNumber = quesNumber + 1
    print("Your score:", score)


main()

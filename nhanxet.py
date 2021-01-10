import random
yep = 0
nope = 0
seperator = ', '
paragraph = ''

def converttostr(input_seq, seperator):
    final_str = seperator.join(input_seq)
    return final_str

print('=======================================')

quest = input("Grammar: [Y/N] ")
if quest == 'y' or quest == 'Y':
    yep = yep + 1
    paragraph += 'Con nhớ cấu trúc câu tốt.'
elif quest == 'n' or quest == 'N':
    option = input("Why: ")
    if option == '':
        nope = nope + 2
        paragraph += 'Con đôi lúc còn mất tập trung nên chưa nắm được các cấu trúc hôm nay được dạy, con cố gắng về học lại nhé.'
    elif option == 'q':
        list = []
        n = int(input("Nnumber of grammar errors: "))
        for i in range(0, n):
            print("Enter error No.{}: ".format(i+1))
            elm = input()
            list.append(elm)
        nope = nope + 1
        rand = random.randint(1,2)
        if rand == 1:
            paragraph += 'Con đã nắm được cấu trúc câu được học nhưng ' + converttostr(list, seperator) + '.'
        elif rand == 2:
            paragraph += 'Con đã hiểu các cấu trúc được học nhưng ' + converttostr(list, seperator) + '.'

print('=======================================')

quest = input("Spelling: [Y/N] ")
if quest == 'y' or quest == 'Y':
    yep = yep + 1
    paragraph += ' Con đã phát âm ổn các từ hôm nay học.'
elif quest == 'n' or quest == 'N':
    option = input("Why: ")
    if option == '':
        nope = nope + 2
        paragraph += ' Con đôi lúc còn mất tập trung nên chưa chú ý học phát âm cùng các bạn.'
    elif option == 'q':
        list = []
        n = int(input("Number of spelling mistakes: "))
        for i in range(0, n):
            print("Enter mistake No.{}: ".format(i+1))
            elm = input()
            list.append(elm)
        nope = nope + 1
        rand = random.randint(1,2)
        if rand == 1:
            paragraph += ' Con hiểu cách phát âm nhưng đọc chưa đúng ' + converttostr(list, seperator) + '.'
        elif rand == 2:
            paragraph += ' Con biết phát âm nhiều từ được học nhưng con ' + converttostr(list, seperator) + '.'

print('=======================================')

quest = input("New Words: [Y/N] ")
if quest == 'y' or quest == 'Y':
    yep = yep + 1
    paragraph += ' Con nhớ từ và tiếp thu ý nghĩa các từ tốt.'
elif quest == 'n' or quest == 'N':
    option = input("Why: ")
    if option == '':
        nope = nope + 2
        paragraph += ' Con chưa chú ý trong giờ nên quên khá nhiều tứ được dạy, con cố gắng về học lại nhé.'
    elif option == 'q':
        list = []
        n = int(input("Number of New words missed: "))
        for i in range(0, n):
            print("Enter missed word No.{}: ".format(i+1))
            elm = input()
            list.append(elm)
        nope = nope + 1
        rand = random.randint(1,2)
        if rand == 1:
            paragraph += ' Con đã nhớ một số từ nhưng con còn quên ' + converttostr(list, seperator) + '.'
        elif rand == 2:
            paragraph += ' Con đã nắm ý nghĩa của các từ nhưng con còn quên ' + converttostr(list, seperator) + '.'

print('=======================================')

quest = input("Homework: [Y/N] ")
if quest == '':
    yep = yep + 1
elif quest == 'n' or quest == 'N':
    nope = nope + 1
    rand = random.randint(1,2)
    if rand == 1:
        paragraph += ' Con cố gắng làm bài về nhà trước giờ học nhé.'
    elif rand == 2:
        paragraph += ' Con chú ý hoàn thành bài tập trước khi đến lớp nhé.'

print('=======================================')

quest = input("Attitude: [Y/N] ")
if quest == 'y' or quest == 'Y':
    yep = yep + 1
    rand = random.randint(1,3)
    if rand == 1:
        paragraph += ' Con hăng hái tham gia các hoạt động của lớp.'
    elif rand == 2:
        paragraph += ' Con năng nổ trong giờ học.'
    elif rand == 3:
        paragraph += ' Con ngoan, tập trung nghe giảng.'
elif quest == 'n' or quest == 'N':
    nope = nope + 1
    rand = random.randint(1,3)
    if rand == 1:
        paragraph += ' Con còn nói chuyện riêng.'
    elif rand == 2:
        paragraph += ' Con đôi lúc mất tập trung và không tích cực tương tác với giáo viên.'
    elif rand == 3:
        paragraph += ' Con chưa năng nổ trả lời bài.'

print('=======================================')

if yep > nope:
    rand = random.randint(1,2)
    if rand == 1:
        paragraph += ' Con học ngoan và tiếp thu tốt, con cố gắng phát huy nhé.'
    elif rand == 2:
        paragraph += ' Con tập trung trong giờ học, tích cực tương tác với giáo viên.'

elif nope > yep:
    rand = random.randint(1,2)
    if rand == 1:
        paragraph += ' Con đã tập trung trong giờ học nhưng con chú ý về ôn lại những phần chưa thuộc cô đã nhận xét bên trên nhé.'
    elif rand == 2:
        paragraph += ' Con nắm được một số phần trong bài học nhưng con cần ôn lại những phần chưa thuộc cô đã nhận xét bên trên nhé.'

print(paragraph)

input("Press Enter to continue...")
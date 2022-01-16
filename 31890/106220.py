state = []
input_count = 0
while True:
    st = input()
    if st == '-----':
        break
    if st.find('voroodi()') != -1:
        input_count += 1
    state.append(st)
inputs = [int(input()) for i in range(input_count)]

counter = []


def NotcheckCounter(item):
    b = counter.count(item)
    if b == 0:
        return(True)
    else:
        return(False)


def changeFunc(item):
    if item.find('voroodi()') != -1:
        st_item = str(item.split('=')[0].strip())
        if NotcheckCounter(st_item):
            counter.append(st_item)
        item = item.replace('voroodi()', 'int('+str(inputs[0])+')')
        inputs.pop(0)
    elif item.find('khoorooji') != -1:
        item = item.replace('khoorooji', 'print')

    elif item.find('agar') != -1:
        item = item.replace('agar', 'if').replace(':', ':\n\t')
        st_item = str(item.split(':')[1].strip().split('=')[0].strip())
        if NotcheckCounter(st_item) == True:
            item += '\n\t s+=1'

    elif item.find('=') != -1:
        st_item = str(item.split('=')[0].strip())
        if NotcheckCounter(st_item):
            counter.append(st_item)

    return item


s = 0

statements = [changeFunc(item) for item in state]
exec('\n'.join(statements))
print(len(counter)+s)

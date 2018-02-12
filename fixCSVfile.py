def hm1('C:\SJU MASTER\DSS 615\Module 2'):
    with open('C:\SJU MASTER\DSS 615\Module 2','r') as f:
        s=f.read().split('\n')
    with open('C:\SJU MASTER\DSS 615\Module 2','w') as f:
        f.write(s[0])
        f.write('\n')
        print(s[0])
        for index , item in enumerate(s[1:-1:2]):
            f.write(item[:-3]+s[2*index+2])
            f.write('\n')
            row=item[:-3].split(',')
            for ss in row[:-1]:
                print(ss.strip(),end=',')
            print(row[-1].strip(),end='')
            row=s[2*index+2][:-4].split(',')
            for ss in row[:-1]:
                # print(ss)
                print(ss.strip(),end=',')
            print(row[-1])
            # input()
if __name__ == '__main__':
    hm1('digestive_illnesses.csv')
def hm2(file):
    with open(file,'r') as f:
        s=f.read().split('\n')
    with open('hm2.csv','w') as f:
        f.write('Description,SNOMED-CT,HCPCS,ICD-10\n')
        print('Description,SNOMED-CT,HCPCS,ICD-10')
        for item in s:
            rows=item.split(',')
            index_set=list(range(len(rows)))
            result=[]
            for feature in ['SNOMED-CT','HCPCS','ICD-10']:
                if feature in rows:
                    i=rows.index(feature)
                    result.append(rows[i+1])
                    index_set.remove(i)
                    index_set.remove(i+1)
                else:
                    result.append('')
            if len(index_set)==1:
                i=index_set[0]
                des=rows[i]
            print(('{},{},{},{}'.format(des,result[0],result[1],result[2])))
            f.write('{},{},{},{}\n'.format(des,result[0],result[1],result[2]))
if __name__ == '__main__':
    hm2('health_codes.csv')
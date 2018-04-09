import tkinter as tk
import lsh_504
import kd_tree

def main():
    global InputFile
    global InputQuery
    global InputQuery
    global LSHResult
    global LSHTime
    global KdTreeResult
    global KdTreeTime
    global lsh2
    global kdtree2
    
    root = tk.Tk()
    root.geometry('600x390')
    root.title('test')
    
    LSHResult = tk.StringVar()
    LSHTime = tk.StringVar()
    KdTreeResult = tk.StringVar()
    KdTreeTime = tk.StringVar()
    
    InputFile = tk.Entry(root, width = 15)
    InputFile.grid(row = 1, column = 1)
    
    InputButton = tk.Button(root, width = 7, height = 2, text = 'Input',
                           command = get_input)
    InputButton.grid(row = 2, column = 1)
    
    InputQuery = tk.Entry(root, width = 45)
    InputQuery.grid(row = 1, column = 2)
    
    QueryButton = tk.Button(root, width = 7, height = 2, text = 'Query',
                           command = get_query)
    QueryButton.grid(row = 2, column = 2)
    
    label0 = tk.Label(root, text = 'LSH result', height = 2)
    label0.grid(row = 3, column = 1)
    
    label1 = tk.Label(root, text = 'LSH time', height = 2)
    label1.grid(row = 6, column = 1)
    
    label2 = tk.Label(root, text = 'Kd-tree result', height = 2)
    label2.grid(row = 7, column = 1)
    
    label3 = tk.Label(root, text = 'Kd-tree time', height = 2)
    label3.grid(row = 10, column = 1)
    
    label4 = tk.Label(root, textvariable = LSHResult, height = 6)
    label4.grid(row = 3, column = 2)
    
    label5 = tk.Label(root, textvariable = LSHTime, height = 2)
    label5.grid(row = 6, column = 2)
    
    label6 = tk.Label(root, textvariable = KdTreeResult, height = 6)
    label6.grid(row = 7, column = 2)
    
    label7 = tk.Label(root, textvariable = KdTreeTime, height = 2)
    label7.grid(row = 10, column = 2)
    
    root.mainloop()
    
def get_input():
    global InputFile
    global InputQuery
    global LSHResult
    global LSHTime
    global KdTreeResult
    global KdTreeTime
    global lsh2
    global kdtree2
    
    FileName = InputFile.get()
    lsh2 = lsh_504.get_lshash(FileName)
    kdtree2 = kd_tree.kdtree(FileName)
    LSHResult.set('Please input query data')
    LSHTime.set('Please input query data')
    KdTreeResult.set('Please input query data')
    KdTreeTime.set('Please input query data')
    #print('get data')

    
def get_query():
    global InputQuery
    global LSHResult
    global LSHTime
    global KdTreeResult
    global KdTreeTime
    global lsh2
    global kdtree2
    data = InputQuery.get()
    print("----------")
    print(lsh2)
    print("----------")
    ans1 = []
    print("----------")
    print(lsh_504.lsh_query(data,lsh2))
    print("----------")
    print(ans1)
    print("---------- ans1")
    ans1 = lsh_504.lsh_query(data,lsh2)
    a1 = ans1[0]
    b1 = ans1[1]
    c1 = ans1[2]
    LSHResult.set(a1 + '\n' + c1)
    LSHTime.set(b1)

    ans2 = []
    ans2 = kd_tree.result(data,kdtree2)
    a2 = ans2[0]
    b2 = ans2[1]
    c2 = ans2[2]
    KdTreeResult.set(a2 + '\n' + c2)
    KdTreeTime.set(b2)
    #print('get query')

if __name__ == '__main__':
    main()

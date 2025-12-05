# def hello():
#     yield 1
#     yield 2 
#     yield 3
# helloitem = hello()
# print(next(helloitem))
# print(next(helloitem))


# def my_range(n):
#     count = 0
#     while count <= n:
#         yield count
#         count+=1
# a =[1,2,3,4]

# for i in my_range(10):
#     print(i)
    


def my_range(start,end):
    end = start+end-1
    count = start
    while (count >= start)and(count <= end):
        yield count
        count+=1
 


for i in my_range(10):

    print(i)
    
# def balls():
#     for i in range(10000000000):
#         yield i
# ballres = balls()
# # print(next(ballres))
# # print(next(ballres))
# # print(next(ballres))
# # print(next(ballres))

# for iem in range(100):
#     print(next(ballres))





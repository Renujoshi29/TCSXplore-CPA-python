class Movie:
    def __init__(self, movie_id, movie_name, ticket_cost, cost_category="Default" ):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.ticket_cost = ticket_cost
        self.cost_category = cost_category

    def Price_category(self):
        if self.ticket_cost>0 and self.ticket_cost<150:
            self.cost_category="General"
        elif self.ticket_cost>=150 and self.ticket_cost<250:
            self.cost_category="Silver"
        elif self.ticket_cost>=250 and self.ticket_cost<350:
            self.cost_category="Gold"
        else:
            self.cost_category="Platinum"

class Movie_ticket:
    def __init__(self, customer_name, movName, viewerCount, totalTicketCost):
        self.customer_name = customer_name
        self.movName = movName
        self.viewerCount = viewerCount
        self.totalTicketCost = totalTicketCost

def getCategoryWiseCount(movieList):
    for i in movieList:
        i.Price_category()
    dict={}
    #below steps are creating dict as category:count as key:value pair
    for i in movieList:
        cat=i.cost_category
        if cat not in dict.keys():
            dict[cat]=1 #this is making the count of each category 1
        else:
            dict[cat]+=1 #this is increasing the count thereafter every category addition
    return dict

def bookMovieTicket(movieList, customer_name, movName, viewerCount):
    for i in movieList:
        tix = i.movie_name.lower() == movName.lower()
        if(tix):
            totalTicketCost=i.ticket_cost*viewerCount
            return totalTicketCost

if __name__ == '__main__':
    movieList=[]
    n=int(input())
    for i in range(n):
        movie_id=int(input())
        movie_name=input()
        ticket_cost=int(input())
        movieObject=Movie(movie_id, movie_name, ticket_cost)
        movieList.append(movieObject)

    customer_name=input()
    movName=input()
    viewerCount=int(input())

    count=getCategoryWiseCount(movieList)
    print("Category wise Count")
    for i in count:
        print('{}:{}'.format(i,count[i]))

    display=bookMovieTicket(movieList, customer_name, movName, viewerCount)
    print(customer_name,display)

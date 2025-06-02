

# Predefined Crypto Data
class CryptoAI:
    def __init__(self):

        self.crypto_db = {  
            "Bitcoin": {  
                "price_trend": "rising",  
                "market_cap": "high",  
                "energy_use": "high",  
                "sustainability_score": 3/10  
            },  
            "Ethereum": {  
                "price_trend": "stable",  
                "market_cap": "high",  
                "energy_use": "medium",  
                "sustainability_score": 6/10  
            },  
            "Cardano": {  
                "price_trend": "rising",  
                "market_cap": "medium",  
                "energy_use": "low",  
                "sustainability_score": 8/10  
            }  
        } 

# Step 3 & 4: Chatbot logic with advice rules
    def respond(self,user_query):
        query= user_query.lower()
        if "sustainable" in query or "eco" in query:
            recommend = max(self.crypto_db,key=lambda x:self.crypto_db[x] ["sustainability_score"])
            score = self.crypto_db[recommend]["sustainability_score"]*10
            return f"I recommend{recommend} It is eco friendly with a sustainability score of{score}/10"
        
        elif "trending" in query or "rising" in query:
            trending =[coin for coin in self.crypto_db if self.crypto_db[coin]["price_trend"]=="rising"]
            return f"These coins are trending {' ,'.join (trending)}"
        
        elif "long term" in query or  "growth":
            for coin,data in self.crypto_db.items():
                if data["price_trend"]=="rising" and data["price_trend"]=="sustainability_score" >0.7:
                    return f"{coin} is a great pick for long-term growth—strong trends and sustainable!"
            return f"none currently stand out for long-term growth"
        
        elif "profitable" in query or "investment" in query:
            for coin,data  in self.crypto_db.items():
                if data["price_trend"]=="rising" and data["market_cap"] == "high":
                    return f"{coin} is profitable"
            return f"none currently profitable coin"

        elif "all data" in query:
            return "\n".join ([f"{coin}:{data}" for coin,data in self.crypto_db.items()]) 

        else:
            return f"I didnt get  your question, Try asking about trends, sustainability, or investment tips!" 


cryptochatbot = CryptoAI()
# Define its personality
print("Hey there welcome to cryptoAI")
print("Get your best crypto advises from me")
while True:
    user_input = input("You: ")
    if user_input.lower()in['Exit','quit']:
        print("cryptochatbot:Goodbye!")
        break
    print("cryptochatbot:", cryptochatbot.respond(user_input))

if __name__ == "__main__":
    bot = CryptoAI()
    
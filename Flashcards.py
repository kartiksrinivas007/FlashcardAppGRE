 
from tqdm import tqdm
import pickle
from argparse import ArgumentParser
import os
class Flashcards:
    def __init__(self, data, weak_list) -> None:
        self.data = data
        self.weak_list = weak_list
        self.weak_list = list(set(self.weak_list))
        pass
        
    def show_question(self, index):
        return self.data[index]["question"]
    
    def show_answer(self, index):
        return self.data[index]["answer"]
    
    def update(self, index):
        print("Enter updated question:")
        question = input()
        print("Enter updated answer:")
        answer = input()
        # print("Enter updated level:")
        # level = input()
        self.data[index] = {"question": question, "answer": answer}
        self.save()
        pass
    
    def add_card(self, question, answer):
        self.data.append({"question": question, "answer": answer})
        pass
    
    def save(self):
        with open(args.path, "wb") as f:
            pickle.dump(self.data, f)
    
    def add_cards(self):
        while(True):
            print("Enter question:")
            question = input()
            print("Enter answer or q to quit:")
            answer = input()
            # print("Enter level:")
            # level = input()
            if(answer == "q"):
                break
            self.add_card(question, answer)
        self.save()
         ### push and commit to git
         
        os.system(f"git add {args.path}")
        os.system("git commit -m 'added new flashcards'")
        os.system("git push -u origin master")
        pass
    
    def test(self, args):
        corr_count = 0
        if(args.test == True):
            for i in tqdm(range(args.start_index, len(self.data))):
                print(self.show_question(i))
                result = input()
                if(result == "q"):
                    break
                elif(result == ""):
                    corr_count += 1
                elif(result == "u"):
                    self.update(i)
                elif(result == "n"):
                    self.weak_list.append(i)
                    pass
                else:
                    pass
                
                # print("Enter level")
                # level = input()
                # self.data[i]["level"] = level
                print(self.show_answer(i))
                
            self.weak_list = list(set(self.weak_list))
            pickle.dump(self.weak_list, open("weak.pkl", "wb"))
            print("Correct count: ", corr_count)
        if(args.weak == True):
            print("Weak flashcards:")
            for i in tqdm(self.weak_list):
                print(self.show_question(i))
                result = input()
                if(result == "q"):
                    break
                elif(result == ""):
                    corr_count += 1
                elif(result == "u"):
                    self.update(i)
                elif(result == "n"):
                    self.weak_list.append(i)
                    pass
                else:
                    pass
                print(self.show_answer(i))
            self.weak_list = list(set(self.weak_list))
            pickle.dump(self.weak_list, open("weak.pkl", "wb"))
        os.system(f"git add {args.path}")
        os.system("git add weak.pkl")
        os.system("git commit -am 'added new flashcards'")
        os.system("git push -u origin master")
    
    def show_related(self, word):
        for i in tqdm(range(len(self.data))):
            if(word in self.show_question(i) or word in self.show_answer(i)):
                print(self.show_question(i))
                input()
                print(self.show_answer(i))
                for k in [-2,-1,0,1,2]:
                    try:
                        print(self.show_question(i+k))
                        input()
                        print(self.show_answer(i+k))
                    except:
                        pass
        pass
if __name__ == "__main__":
    
    ### create data.pkl if it does not exist
    
    parser = ArgumentParser(description="Flashcard addition or testing for Vocabulary")
    parser.add_argument("-a", "--add", action="store_true", help="Add flashcards")
    parser.add_argument("-t", "--test", action="store_true", help="Test flashcards")
    parser.add_argument("-w", "--weak", action="store_true", help="Test weaker flashcards")
    parser.add_argument("-s", "--search", action="store_true", help="Search for a word")
    parser.add_argument("-i", "--start_index", type=int, default=0, help="Start index for testing")
    parser.add_argument("-p", "--path", type=str, default="data.pkl", help="Path to the data list to create")
    parser.set_defaults(add=False)
    parser.set_defaults(test=False)
    parser.set_defaults(weak=False)
    parser.set_defaults(search=False)
    args = parser.parse_args()
        
    try:
        with open(args.path, "rb") as f:
            pass
    except:
        with open(args.path, "wb") as f:
            pickle.dump([], f)
            
    try:
        with open("weak.pkl", "rb") as f:
            pass
    except:
        with open("weak.pkl", "wb") as f:
            pickle.dump([], f)
    
    with open(args.path, "rb") as f:
        data = pickle.load(f)
        
    with open("weak.pkl", "rb") as f:
        weak_list = pickle.load(f)
        
    
    Flashcards = Flashcards(data, weak_list)
    
    if(args.add):
        Flashcards.add_cards()
    elif(args.search):
        print("Enter word to search:")
        word = input()
        Flashcards.show_related(word)
    else:
        Flashcards.test(args)
    pass
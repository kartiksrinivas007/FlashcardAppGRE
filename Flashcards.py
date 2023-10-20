 
from tqdm import tqdm
import pickle
from argparse import ArgumentParser

class Flashcards:
    def __init__(self, data) -> None:
        self.data = data
        pass
        
    def show_question(self, index):
        return self.data[index]["question"]
    
    def show_answer(self, index):
        return self.data[index]["answer"]
    
    def add_card(self, question, answer):
        self.data.append({"question": question, "answer": answer})
        pass
    
    def save(self):
        with open("data.pkl", "wb") as f:
            pickle.dump(self.data, f)
    
    def add_cards(self):
        while(True):
            print("Enter question:")
            question = input()
            print("Enter answer or q to quit:")
            answer = input()
            if(answer == "q"):
                break
            self.add_card(question, answer)
        self.save()
        pass
    
    def test(self):
        corr_count = 0
        for i in tqdm(range(len(self.data))):
            print(self.show_question(i))
            result = input()
            if(result == "q"):
                break
            elif(result == "c"):
                corr_count += 1
            else:
                pass
            print(self.show_answer(i))
        pass

if __name__ == "__main__":
    
    ### create data.pkl if it does not exist
    
    parser = ArgumentParser(description="Flashcard addition or testing for Vocabulary")
    parser.add_argument("-a", "--add", action="store_true", help="Add flashcards")
    parser.add_argument("-t", "--test", action="store_true", help="Test flashcards")
    parser.set_defaults(add=False)
    args = parser.parse_args()
        
    try:
        with open("data.pkl", "rb") as f:
            pass
    except:
        with open("data.pkl", "wb") as f:
            pickle.dump([], f)
    
    with open("data.pkl", "rb") as f:
        data = pickle.load(f)
        
    
    Flashcards = Flashcards(data)
    if(args.add):
        Flashcards.add_cards()
    else:
        Flashcards.test()
    pass
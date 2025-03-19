class Election_Commission:
    def __init__(self, first_candidate, second_candidate, max_voters):
        self.first_candidate = first_candidate
        self.second_candidate = second_candidate
        self.max_voters = max_voters

class VotingProcess(Election_Commission):
    def __init__(self, first_candidate, second_candidate, max_voters):
        super().__init__(first_candidate, second_candidate, max_voters)
        self.candidate_results = {self.first_candidate: 0, self.second_candidate: 0}
        self.voter_ids = set() 
    
    def display_candidates(self):
        print(f"1. {self.first_candidate}")
        print(f"2. {self.second_candidate}")
    
    def handle_task(self, voter_id, choice):
        if voter_id in self.voter_ids:
            print("Voter ID already used, vote not accepted!")
        
        elif choice == 1:
            print(f"You voted for {self.first_candidate}!")
            self.candidate_results[self.first_candidate] += 1
        elif choice == 2:
            print(f"You voted for {self.second_candidate}!")
            self.candidate_results[self.second_candidate] += 1
        else:
            print("Invalid choice!")
            return False
        
        self.voter_ids.add(voter_id)
        
        return True

def main():
    first_candidate = input("\nEnter the first candidate's name: ")
    second_candidate = input("\nEnter the second candidate's name: ")
    max_voters = int(input("\nEnter the number of voters: "))

    election = Election_Commission(first_candidate, second_candidate, max_voters)
    
    voting = VotingProcess(election.first_candidate, election.second_candidate, election.max_voters)
    
    while len(voting.voter_ids) < voting.max_voters:
        print("\n--- Election Voting ---")
        voting.display_candidates()
        
        try:
            voter_id = int(input("\nEnter your Voter ID: "))
            choice = int(input("Enter your Choice (1 or 2): "))
            
            if not voting.handle_task(voter_id, choice):
               break
        except ValueError:
            print("Invalid input, please enter numeric values for voter ID and choice.")
    
    print("\nElection Over!")
    print("Final Results:")
    print(f"{first_candidate}: {voting.candidate_results[first_candidate]} votes")
    print(f"{second_candidate}: {voting.candidate_results[second_candidate]} votes")

if __name__ == "__main__":
    main()

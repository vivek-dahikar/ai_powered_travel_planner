from crew import AiPoweredTravelPlanner

destination = input("Enter your destination: ")
interests = input("Enter your interests (e.g., history, adventure, food): ")
cuisine_preferences = input("Enter your preferred cuisine: ")

crew = AiPoweredTravelPlanner()

result = crew.crew().kickoff(inputs={
    "destination": destination,
    "interests": interests,
    "cuisine_preferences": cuisine_preferences
})

print(result)

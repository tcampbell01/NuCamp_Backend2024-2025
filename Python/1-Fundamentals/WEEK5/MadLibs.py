import random


class Gather_Input:
    def __init__(self):
        self.nouns = []
        self.verbs = []
        self.adjectives = []
        self.adverbs = []
        self.plural_nouns = []
        self.animals = []
        self.celebrity_males = []
        self.celebrity_females = []
        self.places = []
        self.type_of_containers = []
        self.something_gross = []
        self.verb_ending_in_ing = []
        self.type_of_food = []
        self.numbers = []
        self.colors = []

        # Collect input from the user
        self.collect_input()

    def collect_input(self):
        """Collects all necessary words from the user."""
        word_types = [
            'nouns', 'verbs', 'adjectives', 'adverbs', 'plural_nouns', 'animals', 'celebrity_males', 'celebrity_females',
            'places', 'type_of_containers', 'something_gross', 'verb_ending_in_ing', 'type_of_food', 'numbers', 'colors'
        ]

        for word_type in word_types:
            while True:
                # Prompt the user for input
                user_input = input(
                    f"""
                    Please enter at least 5 {word_type}. Follow each one with a comma.
                    Press Enter when you are finished! If you would like to exit the program, press 'x':
                    """
                )

                # Check if the user wants to exit
                if user_input.lower() == 'x':
                    print("Exiting the program...")
                    exit()  # Exit the program if 'x' is pressed

                # Split the input string by commas, strip extra spaces from each word, and create a list
                word_list = [
                    word.strip()
                    for word in user_input.split(',')
                    if word.strip()
                ]

                # Check if at least 5 words were entered
                if len(word_list) >= 5:
                    # Add the list of words to the corresponding attribute of the class
                    getattr(self, word_type).extend(word_list)

                    # Print the current list after each iteration
                    print(
                        f"\nCurrent {word_type.capitalize()} list: "
                        f"{getattr(self, word_type)}\n"
                    )

                    break  # Exit the loop if valid input is provided
                else:
                    print(f"""
                        Sorry, you need to enter at least 5 {word_type}.
                        You entered {len(word_list)}. Please try again.
                    """)

    def generate_random_story(self):
        """Generate a random Mad Libs story using the collected words."""
        # Story templates with placeholders
        story_templates = [
            """
            Albert Einstein, the son of {celebrity_male} and {celebrity_female}, was born in Ulm, Germany in 1879. In 1902, he had a job as an assistant {noun} at the Swiss Patent Office and attended the University of Zurich.
            There he began studying atoms, molecules, and {plural_nouns}. He developed his famous theory of {adjective} relativity, which expanded the phenomena of subatomic {plural_nouns} and {adjective} magnetism. In 1921, he won the Nobel Prize in {plural_nouns} and was director of theoretical physics at the Kaiser Wilhelm {noun} in Berlin.
            In 1933, when Hitler became chancellor of the {place}, Einstein came to America to take a post at the Institute for {plural_nouns} in Princeton, NJ, where his theories helped America devise the first atomic {noun}. There is no question about it: Einstein was one of the most brilliant {plural_nouns} of our time.
            """,

            """
            Everyone knows that kids who eat junk food turn out {adverb}. Make sure your lunch {type_of_container} is filled with nutritious, {adjective} food. Do not go to the {adjective}-food stand across the street from your school.
            The hamburgers they serve are fried in {something_gross} and are made of {animal} meat. The hot dogs contain chemicals such as hydrogenated {noun} and sodium {noun}. 
            And they are made from ground-up {plural_nouns}. If you spend time {verb_ending_in_ing} around those places, you will get fat and {adjective}, and people will call you a/an {noun}.
            So take a sandwich made of chicken or turkey, or lettuce, {type_of_food}, and {plural_nouns}. And drink healthy {animal} milk instead of cola drinks. If you eat good food, you might grow up to become president of {place}.
            """,

            """
            Ladies and {plural_nouns}, please {verb} this way as we begin our tour of the {color} House, the {adjective} home of our nation's {noun}.
            It has more than {number} rooms! The {noun} Room, where huge, {adjective} {plural_nouns} are held, is the largest. Throughout the mansion, you will find portraits of previous {plural_nouns} who {verb}ed here. Upstairs, you can see the famous Lincoln {noun}, where the ghost of {celebrity_male} has often been seen {verb_ending_in_ing}.
            The president's {noun} is in the West Wing and is shaped like a/an {noun}.
            """
        ]

        # Randomly select one story template
        chosen_story_template = random.choice(story_templates)

        # Randomly select words for the story
        story = chosen_story_template.format(
            noun=random.choice(self.nouns),
            verb=random.choice(self.verbs),
            adjective=random.choice(self.adjectives),
            adverb=random.choice(self.adverbs),
            plural_nouns=random.choice(self.plural_nouns),
            animal=random.choice(self.animals),
            celebrity_male=random.choice(self.celebrity_males),
            celebrity_female=random.choice(self.celebrity_females),
            place=random.choice(self.places),
            type_of_container=random.choice(self.type_of_containers),
            something_gross=random.choice(self.something_gross),
            verb_ending_in_ing=random.choice(self.verb_ending_in_ing),
            type_of_food=random.choice(self.type_of_food),
            number=random.choice(self.numbers),
            color=random.choice(self.colors)
        )

        print("\nHere's your Mad Libs story:\n")
        print(story)


# Create an instance of Gather_Input to start the program
gather = Gather_Input()
gather.generate_random_story()

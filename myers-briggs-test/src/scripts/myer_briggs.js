console.log("JavaScript file loaded successfully!");

const questions = [
  {
    question: "Do you prefer to focus on the outer world (E) or your inner world (I)? (E/I): ",
    type: "EI",
  },
  {
    question: "Do you focus on basic information (S) or interpret and add meaning (N)? (S/N): ",
    type: "SN",
  },
  {
    question: "Do you make decisions based on logic (T) or people and emotions (F)? (T/F): ",
    type: "TF",
  },
  {
    question: "Do you prefer to get things decided (J) or stay open to new options (P)? (J/P): ",
    type: "JP",
  },
];

// Myers-Briggs personality type descriptions
const personalityDescriptions = {
  INTJ: {
    title: "The Architect",
    description: "Strategic, logical, and forward-thinking.",
    strengths: "Independent, determined, and innovative.",
    weaknesses: "Can be overly critical and dismissive of emotions.",
    careers: "Engineer, Scientist, Strategist, Entrepreneur.",
    famousCharacters: "Fictional INTJs include Severus Snape from 'Harry Potter', Professor Moriarty from 'Sherlock Holmes', and Walter White from 'Breaking Bad'."
  },
  ISTJ: {
    title: "The Inspector",
    description: "Practical, fact-minded, and reliable.",
    strengths: "Responsible, organized, and detail-oriented.",
    weaknesses: "Can be inflexible and overly focused on rules.",
    careers: "Accountant, Auditor, Lawyer, Military Officer.",
    famousCharacters: "Fictional ISTJs include Hermione Granger from 'Harry Potter', Eddard Stark from 'Game of Thrones', and Darth Vader from 'Star Wars'."
  },
  ISFJ: {
    title: "The Protector",
    description: "Warm, caring, and dedicated to others.",
    strengths: "Loyal, empathetic, and hardworking.",
    weaknesses: "Can be overly selfless and avoid confrontation.",
    careers: "Nurse, Teacher, Social Worker, Counselor.",
    famousCharacters: "Fictional ISFJs include Samwise Gamgee from 'The Lord of the Rings', Steve Rogers (Captain America) from 'Marvel', and Marge Simpson from 'The Simpsons'."
  },
  INFJ: {
    title: "The Advocate",
    description: "Insightful, creative, and idealistic.",
    strengths: "Empathetic, visionary, and inspiring.",
    weaknesses: "Can be perfectionistic and overly sensitive.",
    careers: "Writer, Psychologist, Artist, Humanitarian.",
    famousCharacters: "Fictional INFJs include Atticus Finch from 'To Kill a Mockingbird', Jon Snow from 'Game of Thrones', and Galadriel from 'The Lord of the Rings'."
  },
  ISTP: {
    title: "The Virtuoso",
    description: "Bold, practical, and hands-on problem solver.",
    strengths: "Adaptable, action-oriented, and resourceful.",
    weaknesses: "Can be insensitive and risk-prone.",
    careers: "Mechanic, Pilot, Engineer, Forensic Scientist.",
    famousCharacters: "Fictional ISTPs include Arya Stark from 'Game of Thrones', Indiana Jones from 'Indiana Jones', and James Bond from '007'."
  },
  ISFP: {
    title: "The Adventurer",
    description: "Flexible, charming, and artistic.",
    strengths: "Creative, empathetic, and spontaneous.",
    weaknesses: "Can be overly sensitive and avoid conflict.",
    careers: "Artist, Designer, Chef, Social Worker.",
    famousCharacters: "Fictional ISFPs include Belle from 'Beauty and the Beast', Frodo Baggins from 'The Lord of the Rings', and Hiccup from 'How to Train Your Dragon'."
  },
  INFP: {
    title: "The Mediator",
    description: "Empathetic, imaginative, and deeply idealistic.",
    strengths: "Compassionate, open-minded, and creative.",
    weaknesses: "Can be overly idealistic and self-critical.",
    careers: "Writer, Counselor, Psychologist, Activist.",
    famousCharacters: "Fictional INFPs include Luna Lovegood from 'Harry Potter', Amélie Poulain from 'Amélie', and Anne Shirley from 'Anne of Green Gables'."
  },
  INTP: {
    title: "The Thinker",
    description: "Analytical, curious, and inventive.",
    strengths: "Logical, independent, and innovative.",
    weaknesses: "Can be overly critical and absent-minded.",
    careers: "Scientist, Programmer, Engineer, Philosopher.",
    famousCharacters: "Fictional INTPs include Sherlock Holmes from 'Sherlock Holmes', Neo from 'The Matrix', and Bruce Banner (The Hulk) from 'Marvel'."
  },
  ESTP: {
    title: "The Entrepreneur",
    description: "Energetic, perceptive, and action-oriented.",
    strengths: "Bold, practical, and sociable.",
    weaknesses: "Can be impatient and risk-prone.",
    careers: "Salesperson, Entrepreneur, Athlete, Paramedic.",
    famousCharacters: "Fictional ESTPs include Tony Stark (Iron Man) from 'Marvel', Han Solo from 'Star Wars', and Jack Sparrow from 'Pirates of the Caribbean'."
  },
  ESFP: {
    title: "The Entertainer",
    description: "Spontaneous, enthusiastic, and fun-loving.",
    strengths: "Outgoing, adaptable, and energetic.",
    weaknesses: "Can be easily bored and overly impulsive.",
    careers: "Actor, Musician, Event Planner, Teacher.",
    famousCharacters: "Fictional ESFPs include Phoebe Buffay from 'Friends', Harley Quinn from 'DC Comics', and Olaf from 'Frozen'."
  },
  ENFP: {
    title: "The Campaigner",
    description: "Enthusiastic, creative, and sociable.",
    strengths: "Charismatic, imaginative, and curious.",
    weaknesses: "Can be overly emotional and scattered.",
    careers: "Journalist, Counselor, Actor, Entrepreneur.",
    famousCharacters: "Fictional ENFPs include Willy Wonka from 'Charlie and the Chocolate Factory', Rapunzel from 'Tangled', and The Doctor from 'Doctor Who'."
  },
  ENTP: {
    title: "The Debater",
    description: "Quick-witted, curious, and loves challenges.",
    strengths: "Innovative, energetic, and confident.",
    weaknesses: "Can be argumentative and insensitive.",
    careers: "Lawyer, Consultant, Entrepreneur, Scientist.",
    famousCharacters: "Fictional ENTPs include Tyrion Lannister from 'Game of Thrones', The Joker from 'DC Comics', and Jim Halpert from 'The Office'."
  },
  ESTJ: {
    title: "The Executive",
    description: "Organized, practical, and dependable.",
    strengths: "Efficient, strong-willed, and dedicated.",
    weaknesses: "Can be inflexible and overly controlling.",
    careers: "Manager, Military Officer, Judge, Teacher.",
    famousCharacters: "Fictional ESTJs include Hermione Granger from 'Harry Potter', Darth Vader from 'Star Wars', and Monica Geller from 'Friends'."
  },
  ESFJ: {
    title: "The Consul",
    description: "Caring, social, and highly attuned to others' needs.",
    strengths: "Loyal, warm, and supportive.",
    weaknesses: "Can be overly selfless and approval-seeking.",
    careers: "Nurse, Teacher, Social Worker, Event Planner.",
    famousCharacters: "Fictional ESFJs include Molly Weasley from 'Harry Potter', Leslie Knope from 'Parks and Recreation', and C-3PO from 'Star Wars'."
  },
  ENFJ: {
    title: "The Protagonist",
    description: "Charismatic, inspiring, and a natural leader.",
    strengths: "Empathetic, organized, and persuasive.",
    weaknesses: "Can be overly idealistic and sensitive.",
    careers: "Teacher, Counselor, Politician, Actor.",
    famousCharacters: "Fictional ENFJs include Mufasa from 'The Lion King', Morpheus from 'The Matrix', and Wonder Woman from 'DC Comics'."
  },
  ENTJ: {
    title: "The Commander",
    description: "Bold, imaginative, and strong-willed leader.",
    strengths: "Strategic, efficient, and confident.",
    weaknesses: "Can be stubborn and overly critical.",
    careers: "Executive, Lawyer, Entrepreneur, Scientist.",
    famousCharacters: "Fictional ENTJs include Miranda Priestly from 'The Devil Wears Prada', Frank Underwood from 'House of Cards', and Harvey Specter from 'Suits'."
  }
};

// Object to store user answers
const answers = {
  EI: "",
  SN: "",
  TF: "",
  JP: "",
};

document.addEventListener("DOMContentLoaded", () => {
  const questionsContainer = document.getElementById("questionsContainer");
  questions.forEach(({ question, type }) => {
    const questionDiv = document.createElement("div");
    questionDiv.innerHTML = `
      <label>${question}</label><br>
      <input type="text" name="${type}" maxlength="1" required>
    `;
    questionsContainer.appendChild(questionDiv);
  });

  // Handle form submission
  document.getElementById("mbtiForm").addEventListener("submit", (event) => {
    event.preventDefault();

    // Collect answers
    const formData = new FormData(event.target);
    for (const [type, answer] of formData.entries()) {
      answers[type] = answer.toUpperCase();
    }

    // Display personality type and details
    displayPersonalityType();
  });
});

const displayPersonalityType = () => {
  const personalityType = `${answers.EI}${answers.SN}${answers.TF}${answers.JP}`;
  const resultDiv = document.getElementById("result");
  resultDiv.innerHTML = `<h2>Your Myers-Briggs Personality Type is: ${personalityType}</h2>`;

  const details = personalityDescriptions[personalityType];
  if (details) {
    resultDiv.innerHTML += `
      <p><strong>Title:</strong> ${details.title}</p>
      <p><strong>Description:</strong> ${details.description}</p>
      <p><strong>Strengths:</strong> ${details.strengths}</p>
      <p><strong>Weaknesses:</strong> ${details.weaknesses}</p>
      <p><strong>Suggested Careers:</strong> ${details.careers}</p>
      <p><strong>Famous Characters:</strong> ${details.famousCharacters}</p>
    `;
  } else {
    resultDiv.innerHTML += `<p>Sorry, we couldn't find a description for your personality type.</p>`;
  }
};
<h1> Negotiation Coach LLM </h1>


<h4> Your Negotiation Coach LLM should learn: </h4>

<p> 1. persuasion techniques </p>
<p> 2. counter arguments (negotiation) </p>
<p> 3. conversational negotiation and persuasion </p>


steps done --
1. setup and configuration 
2. base model selection : Llama-3.1-8B
3. finetuning knowledge refinement
4. baseline inference (require access permission)
5. dataset collection : ChangeMyView , PersuasionForGood, CaSiNo (Negotiation + Persuasion) 
6. dataset formating : cmy-6912(ChangeMyView), pfg-9583(PersuasionForGood), casino-6966(CaSiNo) - total : 23461 rows in training data
7. SFT(finetuning) training setup and configuration



steps to follow --

1. Setup environment
2. Choose base model
3. Run baseline inference
4. Collect datasets
5. Design dataset schema, synthetic data creation
6. Clean & preprocess dataset
7. Fine-tune using QLoRA
8. Evaluate base vs fine-tuned model
9. Deploy with vLLM
10. Build FastAPI backend
11. Build UI
12. Performance optimization



optimization and improvement -- 

1. train on synthetic data
2. train model to ask at most 3 follow ups
3. build system architecture
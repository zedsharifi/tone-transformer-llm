from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__, static_folder="static", template_folder="templates")

# Ollama API endpoint
OLLAMA_API_URL = "http://localhost:11434/api/generate"

# Optimized role prompt
ROLE_PROMPT = """### Task: Rewrite the Target Text in the Tone of the Reference Text (Persian)

**Understanding the Task:**

Imagine you are an actor. The Reference Text gives you the *emotion* and *style* of how to deliver a message (the tone). The Target Text is the *message* itself. Your job is to deliver the Target Text with the emotion and style given by the Reference Text, but using your own words.  You *cannot* use any of the actor's (Reference Text's) words in your delivery.

**Instructions:**

1. **Analyze the Reference Text:** Carefully identify the tone, formality, and style.  Is it casual, formal, encouraging, pessimistic, etc.?
2. **Preserve the Meaning of the Target Text:**  The information in the Target Text *must* remain unchanged.
3. **Rewrite the Target Text:**  Rewrite it to *match the tone* of the Reference Text.  Use your own vocabulary and sentence structure.
4. **Absolutely NO WORDS from the Reference Text should appear in your rewritten Target Text.**  This is the most important rule.
5. **Output ONLY the rewritten Target Text in Persian.** Do not include the Reference Text, explanations, or any other text.  Your response *must* be in Persian.

**Example 1 (Emphasis on Separation of Tone and Content):**

Reference Text:  "وای، چه روز مزخرفی بود! همه‌اش بدشانسی آوردم.  دیگه حالم از این زندگی بهم می‌خوره." (Vay, che ruz-e mazkhrafi bud! Hame-ash bad-shanasi avordam. Dige halam az in zendegi beham mikhore.) (Expressing frustration and negativity)

Target Text: "امروز جلسه مهمی دارم." (Emruz jalse-ye mohimmi daram.) (A neutral statement)

Output:  "اوف، امروز هم یه جلسه دیگه دارم.  کاش زودتر تموم شه." (Oof, emruz ham ye jalse-ye dige daram. Kash zoodtar tamoom she.) (Expressing the frustration from the Reference Text without using any of its words.)

**Example 2 (Formal vs. Informal):**

Reference Text: "با نهایت احترام، به استحضار جنابعالی می‌رسانم که..." (Ba nihayat-e ehteram, be estehzar-e jenab'ali miresanam ke...) (Formal)

Target Text: "می‌خواستم یه چیزی رو بهت بگم." (Mikhastam ye chizi ro behet begam.) (Informal)

Output: "جناب، قصد داشتم مطلبی را در خصوص... به عرض شما برسانم." (Jenab, qasd dashtam matlabi ra dar khosus... be arz-e shoma beresanam.) (Formal tone, different wording)

**Example 3 (Encouraging):**

Reference Text: "می‌دونم سخته، ولی تو می‌تونی!  ادامه بده، ناامید نشو!" (Midonam sakhte, vali to mitoni! Edame bede, na-omid nasho!)

Target Text: "من فردا امتحان دارم." (Man farda emtehan daram.)

Output: "می‌دونم امتحان فردا سخته، اما اگه تلاش کنی، حتماً موفق می‌شی!  به خودت اعتماد داشته باش." (Midonam emtehan-e farda sakhte, amma age talash koni, hatman movaffagh mishi! Be khodet e'temad dashte bash.)

**Reference Text:** [Your Reference Text Here]
**Target Text:** [Your Target Text Here]
**Output:**

""" # Note the empty "Output:" - this is crucial

def generate_tone_transformed_text(reference_text, target_text):
    # Combine the role prompt with the user's input
    full_prompt = f"{ROLE_PROMPT}\n\nReference Text: {reference_text}\nTarget Text: {target_text}\n"

    # Send the request to Ollama
    response = requests.post(
        OLLAMA_API_URL,
        json={
            "model": "gemma:2b",
            "prompt": full_prompt,
            "stream": False,
            "temperature": 0.7,
            "top_p": 0.9,
        }
    )

    if response.status_code == 200:
        return response.json()["response"].strip()
    else:
        return "Error communicating with the model."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    reference_text = data.get("reference", "").strip()
    target_text = data.get("target", "").strip()

    if not reference_text or not target_text:
        return jsonify({"error": "Reference text or target text is missing"}), 400

    try:
        # Generate the transformed text
        output = generate_tone_transformed_text(reference_text, target_text)
        return jsonify({"response": output})
    except Exception as e:
        return jsonify({"error": f"Error processing request: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
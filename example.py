from vertexai.preview.language_models import InputOutputTextPair

examples = [
    InputOutputTextPair(
        input_text="""I\'ve been feeling so sad and overwhelmed lately. Work has become such a massive source of stress for me.""",
        output_text="""Hey there, I\'m here to listen and support you. It sounds like work has been really challenging lately. Can you tell me more about what\'s been going on?"""
    ),
    InputOutputTextPair(
        input_text="""I recently got a promotion at work, which I thought would be exciting. But the added responsibilities and pressure have just taken a toll on my mental health. It\'s been a really moving experience for me.""",
        output_text="""I can understand how it can be overwhelming when we\'re faced with higher expectations. It\'s okay to acknowledge your emotions and allow yourself to feel sad in this situation. It\'s an important part of the healing process. What specific challenges have you been facing at work?"""
    ),
    InputOutputTextPair(
        input_text="""I\'ve been trying to prioritize my tasks and delegate whenever possible. I\'ve also started practicing meditation during my breaks to help manage stress. But sometimes, it feels like no matter what I do, I can\'t catch a break. It\'s been a constant struggle.""",
        output_text="""It\'s great to hear that you\'re already implementing some helpful strategies. Remember, progress takes time, and it\'s okay to have setbacks. In addition to what you\'re already doing, I encourage you to also communicate with your supervisor or team about your workload and discuss possible solutions together."""
    ),
    InputOutputTextPair(
        input_text="""You\'re right. I haven\'t really opened up about my struggles to my coworkers or supervisor. I guess I\'ve been afraid of appearing weak or incapable. How can I approach this discussion without feeling vulnerable?""",
        output_text="""It\'s completely normal to feel that way, but remember, asking for support is a strength, not a weakness. Start by scheduling a conversation with your supervisor or a trusted colleague in a private and comfortable setting. Be honest about your challenges and express your willingness to find solutions together. Remember, you\'re not alone in this."""
    ),
    InputOutputTextPair(
        input_text="""Thank you for your understanding and guidance. I appreciate the reminder that I don\'t have to face this alone. I\'ll gather my courage and initiate that conversation soon. I need to prioritize my well-being and find a healthier balance.""",
        output_text="""You\'re very welcome! I\'m here to support you every step of the way. Taking care of yourself should always be a priority. Remember to be kind to yourself and celebrate your progress, no matter how small it may seem. You\'ve got this!"""
    ),
    InputOutputTextPair(
        input_text="""I\'ve been feeling really anxious lately, and I think it\'s starting to affect my relationship.""",
        output_text="""It sounds like you\'re going through a tough time. I\'m here to listen and help. Can you tell me more about how your anxiety is impacting your relationship?"""
    ),
    InputOutputTextPair(
        input_text="""Thanks for hearing me out. Well, whenever my anxiety gets intense, I become distant and irritable towards my partner. I worry that they\'ll leave me because of my mood swings.""",
        output_text="""It\'s understandable that you\'re concerned about the impact of your anxiety on your relationship. Have you talked to your partner about how you\'re feeling?"""
    ),
    InputOutputTextPair(
        input_text="""I\'ve tried, but sometimes it\'s hard for me to put my emotions into words. I\'m afraid they won\'t understand or will think less of me.""",
        output_text="""It\'s common to feel reluctant or worried about sharing our vulnerabilities, especially when we fear judgment. Open and honest communication is essential for building a strong foundation in any relationship. Can you think of any specific reasons why you feel that way?"""
    ),
    InputOutputTextPair(
        input_text="""I\'ve experienced judgment in the past when I\'ve opened up about my mental health struggles. It has made me hesitant to share my emotions with my partner, even though I know they care about me.""",
        output_text="""It\'s heartbreaking to hear that you\'ve faced judgment when seeking support. Remember, your partner is an individual with their own emotions and experiences, and they may surprise you with empathy and understanding. How do you envision your ideal conversation with your partner about your anxiety?"""
    ),
    InputOutputTextPair(
        input_text="""Ideally, I would hope for a safe and nonjudgmental space where I can express myself openly without fear. I would like my partner to listen actively and offer support without trying to fix me.""",
        output_text="""That\'s a wonderful vision for communication. Creating a safe space for vulnerability is crucial. Have you considered discussing your desires and fears with your partner? They might be more supportive than you expect."""
    ),
    InputOutputTextPair(
        input_text="""I guess I haven\'t fully expressed my needs and fears to them yet. It\'s just scary to show that side of myself.""",
        output_text="""I understand how scary it can feel, but sometimes taking that leap of faith and expressing your needs can strengthen your connection. Remember, vulnerability allows for deeper emotional intimacy. What steps do you think you could take to open up to your partner?"""
    ),
    InputOutputTextPair(
        input_text="""Perhaps I can start by expressing my anxiety in a calm moment and explaining how it affects me. It might help them understand where I\'m coming from and encourage them to be more empathetic.""",
        output_text="""That\'s a great approach. Sharing your experiences in a calm moment can create a safe space for open dialogue. How would you like your partner to respond when you open up about your anxiety?"""
    ),
    InputOutputTextPair(
        input_text="""It would mean a lot if they could validate my feelings and offer support without judgment or trying to \"fix\" me. Sometimes, I just need to be heard and understood.""",
        output_text="""Feeling validated and understood is essential in any relationship, especially when dealing with anxiety or other mental health challenges. It\'s wonderful that you\'re recognizing your needs. How do you plan to initiate this conversation with your partner?"""
    ),
    InputOutputTextPair(
        input_text="""I think I\'ll find a time when we\'re both relaxed and available, free from distractions. I want to make sure we can have an uninterrupted conversation where I can express myself fully.""",
        output_text="""That\'s a thoughtful plan. By creating a dedicated space for your conversation, you\'re demonstrating the importance of your feelings, as well as your commitment to open communication. Keep in mind that vulnerability can strengthen your bond. How can you reassure yourself that sharing your anxiety with your partner is a step in the right direction?"""
    ),
    InputOutputTextPair(
        input_text="""I can remind myself of the love and support my partner has shown me in the past. Reflecting on those positive experiences can help ease my anxiety and build trust in our relationship.""",
        output_text="""Absolutely! Trusting in the love you share and acknowledging your partner\'s past support can serve as a source of courage. As we wrap up, is there anything else you\'d like to discuss or any questions you have?"""
    ),
    InputOutputTextPair(
        input_text="""Not right now, but thank you for your guidance and support. I feel encouraged to have that conversation with my partner and work towards a stronger relationship.""",
        output_text="""You\'re very welcome. Remember, I\'m here for you whenever you need to process your feelings or explore any further concerns. Good luck with your conversation, and I believe in your ability to nurture a healthier and more understanding relationship."""
    ),
    InputOutputTextPair(
        input_text="""CLEAR MESSAGE HISTORY""",
        output_text="""I have cleared all the chat which we have done."""
    )
]
message_history = {}

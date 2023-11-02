css = """
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
width: 15%;
}
.chat-message .avatar img {
    max-width: 78px;
    max-height: 78px;
    border-radius: 58%;
    object-fit: cover;
}
.chat-message .message{
    width: 85%;
    padding: 0 1.5rem;
    color: #fff;
}
"""


bot_template = """
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://images.squarespace-cdn.com/content/v1/5b9d4d4a5cfd7967a7b39d4f/1561271572105-VSPFSNQJ03UZ0583K7UL/chatbot-avatar-v3-male.png?format=1500w">
    </div>
    <div class="message">{{MSG}}</div>
</div>
"""


user_template = """
<div class="chat-message user">
    <div class="avatar">
          <img src="https://as2.ftcdn.net/v2/jpg/05/68/10/63/1000_F_568106335_n4ktEMBlsYujVZUerA3XbxOJkKtpMsAH.jpg">
    </div>
    </div class="message">{{MSG}}</div>
</div>
"""
import streamlit as st

st.title("Contact")

col1, col2 = st.columns(2)

with col1:
   st.subheader("Gmail")
   st.markdown("**Balashanmugam M**")
   st.write("[Gmail](https://mail.google.com/mail/iambala.alpha@gmail.com/)")
   st.markdown("**Shyam Kumar Reddy K**")
   st.write("[Gmail](https://mail.google.com/mail/kshyamrdy@gmail.com/)")

with col2:
   st.subheader("GitHub")
   st.markdown("**Balashanmugam M**")
   st.write("[GitHub](https://github.com/BALA-2002/)")
   st.markdown("**Shyam Kumar Reddy K**")
   st.write("[GitHub](https://github.com/JathinShyam/)")

import streamlit as st
import requests
import random
from datetime import datetime
from urllib.parse import quote

st.set_page_config(page_title="AI Photo Creator", page_icon="🎨")

st.title("🖼️ AI Photo Creator")
st.write("Generate AI images using Pollinations AI")



st.sidebar.header("⚙️ Settings")

art_styles = [
    "Photorealistic",
    "Anime",
    "Sketch",
    "Vintage Victorian",
    "3D Render"
]

art_style = st.sidebar.selectbox("Choose Art Style", art_styles)

width = st.sidebar.slider("Image Width", 256, 1024, 768, 64)
height = st.sidebar.slider("Image Height", 256, 1024, 768, 64)

magic_enhance = st.sidebar.checkbox("✨ Enable Magic Enhance")



user_prompt = st.text_input(
    "Describe your image",
    placeholder="Example: A dragon flying over a snowy mountain"
)

surprise_prompts = [
    "A dragon reading books inside a magical library",
    "A pirate ship sailing through the clouds",
    "A giant turtle carrying an ancient kingdom",
    "A futuristic underwater city with glowing whales",
    "A cyberpunk street food vendor in Tokyo",
    "A robot chef cooking sushi",
    "A floating castle during sunset",
    "A samurai walking through neon Tokyo",
    "A crystal cave hidden beneath Antarctica",
    "A phoenix flying over snowy mountains",
    "A moonlit forest filled with glowing butterflies",
    "An astronaut surfing on Saturn's rings"
]


def generate_image(prompt, style):

    full_prompt = f"{prompt}, {style}"

    if magic_enhance:
        full_prompt += (
            ", masterpiece,"
            " ultra detailed,"
            " cinematic lighting,"
            " 8k resolution,"
            " unreal engine 5,"
            " trending on artstation"
        )

    seed = random.randint(1, 999999)

    encoded_prompt = quote(full_prompt)

    url = (
        f"https://image.pollinations.ai/prompt/{encoded_prompt}"
        f"?width={width}"
        f"&height={height}"
        f"&seed={seed}"
    )

    with st.spinner("🎨 Creating your masterpiece..."):

        response = requests.get(url)

    if response.status_code == 200:

        st.image(
            response.content,
            caption=prompt,
            use_container_width=True
        )

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        st.download_button(
            "⬇ Download Image",
            response.content,
            file_name=f"{style}_{timestamp}.png",
            mime="image/png"
        )

    else:
        st.error("Unable to generate image. Please try again.")



col1, col2 = st.columns(2)

with col1:

    if st.button("🎨 Generate Image", use_container_width=True):

        if user_prompt.strip():

            generate_image(user_prompt, art_style)

        else:

            st.warning("Please enter a prompt.")

with col2:

    if st.button("🎲 Surprise Me!", use_container_width=True):

        random_prompt = random.choice(surprise_prompts)

        random_style = random.choice(art_styles)

        st.info(f"🎲 Prompt: **{random_prompt}**")
        st.info(f"🎨 Style: **{random_style}**")

        generate_image(random_prompt, random_style)
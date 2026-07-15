import streamlit as st
import requests
import random

st.set_page_config(page_title="AI Image Studio", page_icon="🎨")

st.title("🖼️ AI Photo Creator")
st.write("Generate AI images using Pollinations AI")


st.sidebar.header("⚙️ Settings")

art_style = st.sidebar.selectbox(
    "Choose Art Style",
    [
        "Photorealistic",
        "Anime",
        "Sketch",
        "Vintage Victorian",
        "3D Render"
    ]
)

width = st.sidebar.slider(
    "Image Width",
    min_value=256,
    max_value=1024,
    value=768,
    step=64
)

height = st.sidebar.slider(
    "Image Height",
    min_value=256,
    max_value=1024,
    value=768,
    step=64
)

magic_enhance = st.sidebar.checkbox("✨ Enable Magic Enhance")



user_prompt = st.text_input(
    "Describe your image",
    placeholder="Example: A dragon flying over a snowy mountain"
)



surprise_prompts = [
    "An astronaut riding a horse on Mars",
    "A cyberpunk street food vendor in Tokyo",
    "A giant panda working in an office",
    "A castle floating above the clouds",
    "A futuristic underwater city with glowing whales"
]



if st.button("🎨 Generate Image"):

    if user_prompt != "":

        full_prompt = f"{user_prompt}, {art_style}"

        if magic_enhance:
            full_prompt += ", masterpiece, 8k resolution, highly detailed, trending on artstation, unreal engine 5 render"


        url = f"https://image.pollinations.ai/prompt/{full_prompt}?width={width}&height={height}"

        response = requests.get(url)

        if response.status_code == 200:

            st.image(response.content, caption="Generated Image")


            st.download_button(
                label="⬇ Download Image",
                data=response.content,
                file_name=f"{art_style}_image.png",
                mime="image/png"
            )

        else:
            st.error("Image generation failed.")

    else:
        st.warning("Please enter a prompt.")



if st.button("🎲 Surprise Me!"):

    random_prompt = random.choice(surprise_prompts)

    st.success(f"Prompt: {random_prompt}")

    full_prompt = f"{random_prompt}, {art_style}"

    if magic_enhance:
        full_prompt += ", masterpiece, 8k resolution, highly detailed, trending on artstation, unreal engine 5 render"

    url = f"https://image.pollinations.ai/prompt/{full_prompt}?width={width}&height={height}"

    response = requests.get(url)

    if response.status_code == 200:

        st.image(response.content, caption=random_prompt)

        st.download_button(
            label="⬇ Download Image",
            data=response.content,
            file_name=f"{art_style}_image.png",
            mime="image/png"
        )

    else:
        st.error("Image generation failed.")
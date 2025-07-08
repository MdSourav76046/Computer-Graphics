import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_facecolor('white')

# Remove axes and spines
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
for spine in ax.spines.values():
    spine.set_visible(False)

# Your name
name = "Md Sourav"

# Add text object at center
text = ax.text(0.5, 0.5, name,
               color='blue',
               fontsize=40,
               ha='center',
               va='center')

# Animation function
def animate(frame):
    fps = 60  # frames per second
    stable_duration = 3  # seconds to stay centered
    stable_frames = fps * stable_duration

    if frame < stable_frames:
        x = 0.5
    else:
        slide_frame = frame - stable_frames
        speed = 0.02
        x = (slide_frame * speed) % 1.2
    text.set_position((x, 0.5))
    return text,

# Create animation
ani = animation.FuncAnimation(
    fig, animate, frames=range(2000), interval=1000/30, blit=True)

plt.show()

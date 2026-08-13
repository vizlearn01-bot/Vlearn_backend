import json
from curriculum.models import Lesson, LessonBlock

# -------------------------------------------------------------
# 1. Lesson 195: Matrix Action on Coordinate Vectors (Form 4 Math)
# -------------------------------------------------------------
# Let's ensure all blocks in Lesson 195 are completely humanized and properly formatted.
l195 = Lesson.objects.get(id=195)

# Block 6378: Learning Goal
b = LessonBlock.objects.get(id=6378)
b.content = {
    "text": "Have you ever wondered how video games smoothly rotate a 3D character when you tilt the joystick, how smartphone apps resize and flip photos, or how flight simulators tilt an airplane's wings on screen?\n\nBehind all digital motion and visual effects lies a single elegant mathematical tool: a **$2 \\times 2$ Transformation Matrix**.\n\nThink of a transformation matrix as a **precision coordinate machine**. You feed in any starting point $(x, y)$ on the Cartesian grid, the machine processes it with 4 guiding numbers, and out comes the exact new landing position $(x', y')$ — known as the **image**!\n\n---\n\n### What You Will Master in This Lesson:\n* **The Coordinate Machine Rule**: Learn how to feed a point column vector into a $2 \\times 2$ matrix to calculate its new destination.\n* **Transforming Full Shapes**: Move entire triangles and polygons across the Cartesian plane by transforming their corner vertices.\n* **Mathematical Detective Work**: Work backwards to discover a missing matrix entry when given an object and its image.\n* **Geometric Insight**: Visualize and describe how a matrix rotates, reflects, enlarges, or shears a shape."
}
b.save()

# Block 6379: Concept Explanation
b = LessonBlock.objects.get(id=6379)
b.content = {
    "text": "A **geometric transformation** is simply an operation that maps every point of a shape (the **object**) to a new location on the coordinate plane (the **image**).\n\nTo allow a matrix to act on coordinates, we write any point $P(x, y)$ vertically as a **$2 \\times 1$ column vector**:\n\n$$P = \\begin{pmatrix} x \\\\ y \\end{pmatrix}$$\n\nA **$2 \\times 2$ transformation matrix** consists of four guiding values arranged in two horizontal rows and two vertical columns:\n\n$$M = \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$$\n\n---\n\n### How the Matrix Machine Multiplies:\n\n1. **The Input (Object)**: Load the point's coordinates vertically as $\\begin{pmatrix} x \\\\ y \\end{pmatrix}$.\n2. **The Horizontal Engine (Row 1)**: The top row $(a, b)$ calculates the new $x$-coordinate ($x'$):\n$$x' = ax + by$$\n3. **The Vertical Engine (Row 2)**: The bottom row $(c, d)$ calculates the new $y$-coordinate ($y'$):\n$$y' = cx + dy$$\n4. **The Output (Image)**: Combining the two rows gives the final image position $P'(x', y')$:\n\n$$\\mathbf{\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix} \\begin{pmatrix} x \\\\ y \\end{pmatrix} = \\begin{pmatrix} ax + by \\\\ cx + dy \\end{pmatrix}}$$\n\n*Every single point on the Cartesian plane follows this exact same rule!*"
}
b.save()

# Block 6380: Formula Breakdown
b = LessonBlock.objects.get(id=6380)
b.content = {
    "formula": "$$\\mathbf{\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix} \\begin{pmatrix} x \\\\ y \\end{pmatrix} = \\begin{pmatrix} ax + by \\\\ cx + dy \\end{pmatrix}}$$",
    "content": "| Component | What It Represents | Intuitive Meaning |\n| :--- | :--- | :--- |\n| $\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$ | **Transformation Matrix ($M$)** | The machine controlling how space is shifted, flipped, or turned. |\n| $\\begin{pmatrix} x \\\\ y \\end{pmatrix}$ | **Object Column Vector** | The original point coordinates ($x$ on top, $y$ on bottom). |\n| $\\mathbf{x' = ax + by}$ | **Transformed $x$-coordinate** | First row across multiplied by the column vector down. |\n| $\\mathbf{y' = cx + dy}$ | **Transformed $y$-coordinate** | Second row across multiplied by the column vector down. |\n\n---\n\n### The \"Run Across, Dive Down\" Rule:\n* **For the Top Result ($x'$)**: Run across Row 1 $(a, b)$ and dive down Column $(x, y) \\rightarrow a \\cdot x + b \\cdot y$.\n* **For the Bottom Result ($y'$)**: Run across Row 2 $(c, d)$ and dive down Column $(x, y) \\rightarrow c \\cdot x + d \\cdot y$."
}
b.save()

# Block 6381: Worked Example 1
b = LessonBlock.objects.get(id=6381)
b.content = {
    "problem": "The transformation matrix $M = \\begin{pmatrix} 2 & 1 \\\\ 0 & 3 \\end{pmatrix}$ acts on the point $P(3, 2)$. Find the coordinates of the image point $P'$.",
    "steps": [
        "**Step 1: Write point $P(3, 2)$ as a column vector**\n$$\\begin{pmatrix} x' \\\\ y' \\end{pmatrix} = \\begin{pmatrix} 2 & 1 \\\\ 0 & 3 \\end{pmatrix} \\begin{pmatrix} 3 \\\\ 2 \\end{pmatrix}$$",
        "**Step 2: Calculate the new horizontal coordinate ($x'$)**\nMultiply Row 1 across by the column down:\n$$x' = (2 \\times 3) + (1 \\times 2) = 6 + 2 = 8$$",
        "**Step 3: Calculate the new vertical coordinate ($y'$)**\nMultiply Row 2 across by the column down:\n$$y' = (0 \\times 3) + (3 \\times 2) = 0 + 6 = 6$$",
        "**Step 4: State the final image coordinates**\nThe image column vector is $\\begin{pmatrix} 8 \\\\ 6 \\end{pmatrix}$.\n\n$$\\mathbf{P' = (8, 6)}$$"
    ]
}
b.save()

# Block 6382: Worked Example 2
b = LessonBlock.objects.get(id=6382)
b.content = {
    "problem": "Triangle $PQR$ has vertices $P(1, 0)$, $Q(2, 1)$, and $R(0, 3)$. Under the transformation matrix $T = \\begin{pmatrix} 1 & 2 \\\\ -1 & 0 \\end{pmatrix}$, determine the coordinates of the image triangle $P'Q'R'$.",
    "steps": [
        "**Strategy**: To transform any geometric shape, we feed each corner vertex into matrix $T$ one by one.",
        "**1. Finding Image $P'$ for Vertex $P(1, 0)$**:\n$$\\begin{pmatrix} 1 & 2 \\\\ -1 & 0 \\end{pmatrix} \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix} = \\begin{pmatrix} 1(1) + 2(0) \\\\ -1(1) + 0(0) \\end{pmatrix} = \\begin{pmatrix} 1 \\\\ -1 \\end{pmatrix} \\implies \\mathbf{P'(1, -1)}$$",
        "**2. Finding Image $Q'$ for Vertex $Q(2, 1)$**:\n$$\\begin{pmatrix} 1 & 2 \\\\ -1 & 0 \\end{pmatrix} \\begin{pmatrix} 2 \\\\ 1 \\end{pmatrix} = \\begin{pmatrix} 1(2) + 2(1) \\\\ -1(2) + 0(1) \\end{pmatrix} = \\begin{pmatrix} 4 \\\\ -2 \\end{pmatrix} \\implies \\mathbf{Q'(4, -2)}$$",
        "**3. Finding Image $R'$ for Vertex $R(0, 3)$**:\n$$\\begin{pmatrix} 1 & 2 \\\\ -1 & 0 \\end{pmatrix} \\begin{pmatrix} 0 \\\\ 3 \\end{pmatrix} = \\begin{pmatrix} 1(0) + 2(3) \\\\ -1(0) + 0(3) \\end{pmatrix} = \\begin{pmatrix} 6 \\\\ 0 \\end{pmatrix} \\implies \\mathbf{R'(6, 0)}$$",
        "**Summary Table of the Transformed Triangle**:\n\n| Original Vertex | Matrix Action | Image Vertex |\n| :--- | :--- | :--- |\n| $P(1, 0)$ | $\\begin{pmatrix} 1 & 2 \\\\ -1 & 0 \\end{pmatrix} \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix}$ | $\\mathbf{P'(1, -1)}$ |\n| $Q(2, 1)$ | $\\begin{pmatrix} 1 & 2 \\\\ -1 & 0 \\end{pmatrix} \\begin{pmatrix} 2 \\\\ 1 \\end{pmatrix}$ | $\\mathbf{Q'(4, -2)}$ |\n| $R(0, 3)$ | $\\begin{pmatrix} 1 & 2 \\\\ -1 & 0 \\end{pmatrix} \\begin{pmatrix} 0 \\\\ 3 \\end{pmatrix}$ | $\\mathbf{R'(6, 0)}$ |\n\n**Final Answer**: The image triangle vertices are $\\mathbf{P'(1, -1), Q'(4, -2), R'(6, 0)}$."
    ]
}
b.save()

# Block 6383: Worked Example 3
b = LessonBlock.objects.get(id=6383)
b.content = {
    "problem": "A transformation matrix $M = \\begin{pmatrix} 3 & k \\\\ 1 & 2 \\end{pmatrix}$ maps the object point $A(2, 1)$ onto the image point $A'(8, 4)$. Calculate the value of the unknown entry $k$.",
    "steps": [
        "**Step 1: Set up the matrix multiplication equation**\n$$\\begin{pmatrix} 3 & k \\\\ 1 & 2 \\end{pmatrix} \\begin{pmatrix} 2 \\\\ 1 \\end{pmatrix} = \\begin{pmatrix} 8 \\\\ 4 \\end{pmatrix}$$",
        "**Step 2: Multiply the rows across by the column down**\n* Top row ($x'$): $3(2) + k(1) = 6 + k$\n* Bottom row ($y'$): $1(2) + 2(1) = 2 + 2 = 4$",
        "**Step 3: Equate with the target image coordinates**\n* From the top row:\n$$6 + k = 8$$\n$$k = 8 - 6 = 2$$\n*(Notice that the bottom row gives $4 = 4$, which confirms the equation consistency!)*",
        "**Step 4: Verification Check**\nSubstitute $k = 2$ back into the matrix:\n$$\\begin{pmatrix} 3 & 2 \\\\ 1 & 2 \\end{pmatrix} \\begin{pmatrix} 2 \\\\ 1 \\end{pmatrix} = \\begin{pmatrix} 3(2) + 2(1) \\\\ 1(2) + 2(1) \\end{pmatrix} = \\begin{pmatrix} 8 \\\\ 4 \\end{pmatrix} \\quad \\checkmark$$\n\n$$\\mathbf{k = 2}$$"
    ]
}
b.save()

# Block 6384: Worked Example 4
b = LessonBlock.objects.get(id=6384)
b.content = {
    "problem": "Triangle $ABC$ has vertices $A(0,0)$, $B(4,0)$, and $C(4,3)$. The transformation matrix $T = \\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix}$ maps $ABC$ onto $A'B'C'.$\n\n(a) Find the coordinates of $A', B', C'.$\n(b) Fully describe the transformation geometrically.",
    "steps": [
        "**Part (a): Find the image coordinates**\n* **Image of Origin $A(0, 0)$**:\n$$\\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix} \\begin{pmatrix} 0 \\\\ 0 \\end{pmatrix} = \\begin{pmatrix} 0 \\\\ 0 \\end{pmatrix} \\implies \\mathbf{A'(0, 0)}$$\n*(The origin $(0,0)$ is an invariant point — it never moves under any $2 \\times 2$ matrix!)*\n\n* **Image of $B(4, 0)$**:\n$$\\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix} \\begin{pmatrix} 4 \\\\ 0 \\end{pmatrix} = \\begin{pmatrix} 0(4) + (-1)(0) \\\\ 1(4) + 0(0) \\end{pmatrix} = \\begin{pmatrix} 0 \\\\ 4 \\end{pmatrix} \\implies \\mathbf{B'(0, 4)}$$\n\n* **Image of $C(4, 3)$**:\n$$\\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix} \\begin{pmatrix} 4 \\\\ 3 \\end{pmatrix} = \\begin{pmatrix} 0(4) + (-1)(3) \\\\ 1(4) + 0(3) \\end{pmatrix} = \\begin{pmatrix} -3 \\\\ 4 \\end{pmatrix} \\implies \\mathbf{C'(-3, 4)}$$",
        "**Part (b): Describe the transformation geometrically**\nLet us analyze what happened to the coordinates:\n1. The origin $A(0,0)$ remained fixed.\n2. Point $B(4, 0)$ on the positive $x$-axis swung to $B'(0, 4)$ on the positive $y$-axis — a counter-clockwise rotation of exactly $90^\\circ$.\n3. The shape and dimensions remained identical (isometric transformation).\n\n**Full Geometric Description**:\n$$\\mathbf{\\text{A rotation of } +90^\\circ \\text{ (anticlockwise) about the origin } (0,0)}$$"
    ]
}
b.save()

# Block 6385: Common Misconception
b = LessonBlock.objects.get(id=6385)
b.content = {
    "text": "### 1. The \"Position-by-Position\" Multiplication Trap\n\n❌ **Wrong Thinking**: \"Just multiply the top-left by $x$ and the bottom-right by $y$.\"\n\n✅ **The Reality**: Matrix multiplication combines **entire rows across with columns down**:\n$$x' = ax + by \\quad \\text{and} \\quad y' = cx + dy$$\n\n*(Both numbers in Row 1 contribute to $x'$, and both numbers in Row 2 contribute to $y'$!)*\n\n---\n\n### 2. The \"Flipped Column\" Mistake\n\n❌ **Wrong**: Writing point $P(3, 2)$ as $\\begin{pmatrix} 2 \\\\ 3 \\end{pmatrix}$.\n\n✅ **The Rule**: Always write **$x$ on top** and **$y$ on the bottom** $\\begin{pmatrix} x \\\\ y \\end{pmatrix}$. Flipping them produces a completely wrong image point!\n\n---\n\n### 3. Mixing Up Multiplication Order\n\nAlways follow the action rule: **Matrix $\\times$ Object $=$ Image**.\nNever place the column vector to the left of the $2 \\times 2$ matrix."
}
b.save()

# Block 6386: Knowledge Check 1
b = LessonBlock.objects.get(id=6386)
b.content = {
    "check_type": "multiple_choice",
    "question": "The transformation matrix $M = \\begin{pmatrix} 2 & -1 \\\\ 3 & 0 \\end{pmatrix}$ acts on the point $Q(1, 2)$. What are the coordinates of the image point $Q'$?",
    "options": [
        "$(0, 3)$",
        "$(4, 6)$",
        "$(0, 6)$",
        "$(4, 3)$"
    ],
    "answer": "A",
    "explanation": "**Correct Answer: A $(0, 3)$**\n\nLet us calculate step by step:\n* $x' = 2(1) + (-1)(2) = 2 - 2 = 0$\n* $y' = 3(1) + 0(2) = 3 + 0 = 3$\n\nThus $Q' = (0, 3)$.\n\n* **Why B is incorrect**: It multiplied position-by-position ($2 \\times 1$ and $2 \\times 2$) instead of row $\\times$ column.\n* **Why C is incorrect**: It multiplied the second row by $2$ instead of evaluating $3(1) + 0(2)$.\n* **Why D is incorrect**: It reversed the sign in row 1."
}
b.save()

# Block 6387: Knowledge Check 2
b = LessonBlock.objects.get(id=6387)
b.content = {
    "check_type": "short_answer",
    "question": "Triangle $XYZ$ has vertices $X(2, 0)$, $Y(0, 3)$, and $Z(-1, 1)$. The transformation matrix is $N = \\begin{pmatrix} 1 & 2 \\\\ -1 & 3 \\end{pmatrix}$.\n\nCalculate the coordinates of the image vertices $X', Y', Z'.$",
    "hint": "Multiply matrix $N$ by each vertex column vector: for $X(2, 0)$, calculate $x' = 1(2) + 2(0)$ and $y' = -1(2) + 3(0)$.",
    "answer": "**1. For $X(2, 0)$**:\n$$\\begin{pmatrix} 1 & 2 \\\\ -1 & 3 \\end{pmatrix} \\begin{pmatrix} 2 \\\\ 0 \\end{pmatrix} = \\begin{pmatrix} 1(2)+2(0) \\\\ -1(2)+3(0) \\end{pmatrix} = \\begin{pmatrix} 2 \\\\ -2 \\end{pmatrix} \\implies \\mathbf{X'(2, -2)}$$\n\n**2. For $Y(0, 3)$**:\n$$\\begin{pmatrix} 1 & 2 \\\\ -1 & 3 \\end{pmatrix} \\begin{pmatrix} 0 \\\\ 3 \\end{pmatrix} = \\begin{pmatrix} 1(0)+2(3) \\\\ -1(0)+3(3) \\end{pmatrix} = \\begin{pmatrix} 6 \\\\ 9 \\end{pmatrix} \\implies \\mathbf{Y'(6, 9)}$$\n\n**3. For $Z(-1, 1)$**:\n$$\\begin{pmatrix} 1 & 2 \\\\ -1 & 3 \\end{pmatrix} \\begin{pmatrix} -1 \\\\ 1 \\end{pmatrix} = \\begin{pmatrix} 1(-1)+2(1) \\\\ -1(-1)+3(1) \\end{pmatrix} = \\begin{pmatrix} 1 \\\\ 4 \\end{pmatrix} \\implies \\mathbf{Z'(1, 4)}$$\n\n**Final Coordinates**: $\\mathbf{X'(2, -2), Y'(6, 9), Z'(1, 4)}$."
}
b.save()

# Block 6388: Summary
b = LessonBlock.objects.get(id=6388)
b.content = {
    "text": "### The Core Transformation Formula\n\n$$\\mathbf{\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix} \\begin{pmatrix} x \\\\ y \\end{pmatrix} = \\begin{pmatrix} ax + by \\\\ cx + dy \\end{pmatrix}}$$\n\n---\n\n### 4 Golden Rules for Matrix Transformations:\n1. **Stack Coordinates Vertically**: Always express points as column vectors $\\begin{pmatrix} x \\\\ y \\end{pmatrix}$.\n2. **Row Across, Column Down**: Row 1 dictates the horizontal position ($x'$); Row 2 dictates the vertical position ($y'$).\n3. **Shapes Move Vertex-by-Vertex**: To transform any triangle or polygon, transform each corner point individually.\n4. **The Fixed Origin**: The origin $(0, 0)$ is always fixed at $(0, 0)$ under any $2 \\times 2$ transformation matrix."
}
b.save()

# -------------------------------------------------------------
# 2. Lesson 196: Finding & Interpreting Transformation Matrices
# -------------------------------------------------------------
b = LessonBlock.objects.get(id=6394)
b.content = {
    "problem": "A transformation matrix $T = \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$ maps the point $A(2, 1)$ onto $A'(5, 4)$ and maps $B(1, 2)$ onto $B'(4, 5)$. Find the values of $a, b, c,$ and $d$, and hence write down the transformation matrix $T$.",
    "steps": [
        "**Step 1: Understand why we use simultaneous equations**\nBecause points $A(2, 1)$ and $B(1, 2)$ are general points (not the unit basis points $(1,0)$ or $(0,1)$), we cannot read the matrix columns directly. Instead, we set up two independent pairs of simultaneous equations.",
        "**Step 2: Set up equations for the top row ($a$ and $b$)**\nUsing $x' = ax + by$:\n* From point $A(2, 1) \\to A'(5, 4)$:\n$$2a + b = 5 \\quad \\text{--- (Equation 1)}$$\n* From point $B(1, 2) \\to B'(4, 5)$:\n$$a + 2b = 4 \\quad \\text{--- (Equation 2)}$$",
        "**Step 3: Solve for $a$ and $b$**\n* Multiply Equation 2 by $2$: $$2a + 4b = 8$$\n* Subtract Equation 1 ($2a + b = 5$):\n$$(2a + 4b) - (2a + b) = 8 - 5$$\n$$3b = 3 \\implies \\mathbf{b = 1}$$\n* Substitute $b = 1$ back into Equation 2:\n$$a + 2(1) = 4 \\implies \\mathbf{a = 2}$$",
        "**Step 4: Set up and solve equations for the bottom row ($c$ and $d$)**\nUsing $y' = cx + dy$:\n* From point $A(2, 1) \\to A'(5, 4)$:\n$$2c + d = 4 \\quad \\text{--- (Equation 3)}$$\n* From point $B(1, 2) \\to B'(4, 5)$:\n$$c + 2d = 5 \\quad \\text{--- (Equation 4)}$$\n* Multiply Equation 4 by $2$: $$2c + 4d = 10$$\n* Subtract Equation 3 ($2c + d = 4$):\n$$3d = 6 \\implies \\mathbf{d = 2}$$\n* Substitute $d = 2$ back into Equation 4:\n$$c + 2(2) = 5 \\implies \\mathbf{c = 1}$$",
        "**Step 5: State the final matrix and verify**\n$$\\mathbf{T = \\begin{pmatrix} 2 & 1 \\\\ 1 & 2 \\end{pmatrix}}$$\n\n*Quick Verification*:\n$$\\begin{pmatrix} 2 & 1 \\\\ 1 & 2 \\end{pmatrix} \\begin{pmatrix} 2 \\\\ 1 \\end{pmatrix} = \\begin{pmatrix} 2(2) + 1(1) \\\\ 1(2) + 2(1) \\end{pmatrix} = \\begin{pmatrix} 5 \\\\ 4 \\end{pmatrix} \\quad \\checkmark$$\n$$\\begin{pmatrix} 2 & 1 \\\\ 1 & 2 \\end{pmatrix} \\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix} = \\begin{pmatrix} 2(1) + 1(2) \\\\ 1(1) + 2(2) \\end{pmatrix} = \\begin{pmatrix} 4 \\\\ 5 \\end{pmatrix} \\quad \\checkmark$$"
    ]
}
b.save()

# -------------------------------------------------------------
# 3. Lesson 197: Successive, Identity and Inverse Transformations
# -------------------------------------------------------------
# Block 6401: Concept Explanation
b = LessonBlock.objects.get(id=6401)
b.content = {
    "text": "### What Is a Successive (Composite) Transformation?\n\nWhen you perform multiple transformations in a row (for example: *\"Transformation $A$ **followed by** Transformation $B$\"*), it means:\n1. **First Action**: Apply transformation $A$ to the original shape to produce an intermediate image $P'$.\n2. **Second Action**: Apply transformation $B$ to the intermediate image $P'$ to reach the final image $P''$.\n\n---\n\n### The Single Combined Matrix Formula (Right-to-Left Rule):\n\nInstead of calculating two separate multiplications every time, you can combine them into a single **composite matrix**:\n\n$$\\mathbf{\\text{Composite Matrix for } A \\text{ followed by } B = B \\cdot A}$$\n\n*(Notice that $A$ is written on the **right** because it touches the vector $\\mathbf{x}$ first: $B(A\\mathbf{x}) = (BA)\\mathbf{x}$!)*\n\n---\n\n### Why Sequence Order Really Matters:\n\nIn everyday arithmetic, $3 \\times 5 = 5 \\times 3$. But in geometric matrix transformations, **order changes the destination**:\n\n$$\\mathbf{A \\cdot B \\neq B \\cdot A}$$\n\n$$\\mathbf{\\text{Reflecting then Rotating} \\neq \\text{Rotating then Reflecting}}$$\n\n*Think about it visually! If you flip a shape across a mirror line and then spin it $90^\\circ$, it lands in a completely different position than if you spun it first and flipped it second. Always multiply matrices from **right to left**!*"
}
b.save()

print("Form 4 Mathematics lessons audited and updated successfully!")

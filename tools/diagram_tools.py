"""
Diagram Generation Tools for CBSE Std 9 Learning Agent
Creates visual diagrams for Math, Science, and Geography concepts
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from pathlib import Path
from typing import List, Tuple
import json
import time
import os

# Create diagrams directory
DIAGRAMS_DIR = Path("diagrams")
DIAGRAMS_DIR.mkdir(exist_ok=True)


def cleanup_old_diagrams(max_age_seconds: int = 3600):
    """
    Clean up old diagram files from the diagrams folder
    
    Args:
        max_age_seconds: Maximum age of files to keep (default: 1 hour)
    """
    if not DIAGRAMS_DIR.exists():
        return
    
    current_time = time.time()
    deleted_count = 0
    
    for file_path in DIAGRAMS_DIR.glob("*.png"):
        if file_path.is_file():
            file_age = current_time - file_path.stat().st_mtime
            if file_age > max_age_seconds:
                try:
                    file_path.unlink()
                    deleted_count += 1
                except Exception as e:
                    print(f"Warning: Could not delete {file_path}: {e}")
    
    if deleted_count > 0:
        print(f"Cleaned up {deleted_count} old diagram(s)")


def plot_quadratic_function(a: float, b: float, c: float, filename: str = None) -> str:
    """
    Plot a quadratic function y = ax² + bx + c
    
    Args:
        a: Coefficient of x²
        b: Coefficient of x
        c: Constant term
        filename: Optional custom filename
    
    Returns:
        Path to the saved diagram
    """
    if filename is None:
        filename = f"quadratic_{a}x²+{b}x+{c}.png".replace("-", "neg")
    
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c
    
    plt.figure(figsize=(10, 8))
    plt.plot(x, y, 'b-', linewidth=2, label=f'y = {a}x² + {b}x + {c}')
    plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
    plt.grid(True, alpha=0.3)
    
    # Mark vertex
    vertex_x = -b / (2 * a)
    vertex_y = a * vertex_x**2 + b * vertex_x + c
    plt.plot(vertex_x, vertex_y, 'ro', markersize=10, label=f'Vertex ({vertex_x:.2f}, {vertex_y:.2f})')
    
    # Find and mark x-intercepts (roots) if they exist
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (-b + np.sqrt(discriminant)) / (2*a)
        root2 = (-b - np.sqrt(discriminant)) / (2*a)
        plt.plot([root1, root2], [0, 0], 'go', markersize=8, label='Roots (x-intercepts)')
    
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title(f'Quadratic Function: y = {a}x² + {b}x + {c}', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.ylim(-20, 20)
    
    filepath = DIAGRAMS_DIR / filename
    plt.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close()
    
    return str(filepath.absolute())


def plot_linear_function(m: float, c: float, filename: str = None) -> str:
    """
    Plot a linear function y = mx + c
    
    Args:
        m: Slope
        c: Y-intercept
        filename: Optional custom filename
    
    Returns:
        Path to the saved diagram
    """
    if filename is None:
        filename = f"linear_{m}x+{c}.png".replace("-", "neg")
    
    x = np.linspace(-10, 10, 100)
    y = m * x + c
    
    plt.figure(figsize=(10, 8))
    plt.plot(x, y, 'b-', linewidth=2, label=f'y = {m}x + {c}')
    plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
    plt.grid(True, alpha=0.3)
    
    # Mark y-intercept
    plt.plot(0, c, 'ro', markersize=10, label=f'Y-intercept (0, {c})')
    
    # Mark x-intercept if exists
    if m != 0:
        x_intercept = -c / m
        plt.plot(x_intercept, 0, 'go', markersize=10, label=f'X-intercept ({x_intercept:.2f}, 0)')
    
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title(f'Linear Function: y = {m}x + {c}', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.xlim(-10, 10)
    plt.ylim(-20, 20)
    
    filepath = DIAGRAMS_DIR / filename
    plt.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close()
    
    return str(filepath.absolute())


def draw_cell_diagram(cell_type: str, filename: str = None) -> str:
    """
    Draw a labeled diagram of plant or animal cell
    
    Args:
        cell_type: Either "plant" or "animal"
        filename: Optional custom filename
    
    Returns:
        Path to the saved diagram
    """
    if filename is None:
        filename = f"{cell_type}_cell.png"
    
    fig, ax = plt.subplots(figsize=(12, 10))
    
    if cell_type.lower() == "plant":
        # Plant cell - rectangular with cell wall
        cell_wall = patches.Rectangle((0.5, 0.5), 8, 6, linewidth=4, 
                                      edgecolor='darkgreen', facecolor='lightgreen', alpha=0.3)
        ax.add_patch(cell_wall)
        
        # Cell membrane (inside cell wall)
        cell_membrane = patches.Rectangle((0.7, 0.7), 7.6, 5.6, linewidth=2,
                                         edgecolor='blue', facecolor='none')
        ax.add_patch(cell_membrane)
        
        # Nucleus
        nucleus = patches.Circle((4.5, 3.5), 0.8, edgecolor='purple', 
                                facecolor='lavender', linewidth=2)
        ax.add_patch(nucleus)
        ax.text(4.5, 3.5, 'Nucleus', ha='center', va='center', fontsize=9, fontweight='bold')
        
        # Chloroplasts (multiple)
        for x, y in [(2.5, 2), (6.5, 2), (2, 4.5), (7, 4.5), (3.5, 5.5), (5.5, 1.5)]:
            chloroplast = patches.Ellipse((x, y), 0.6, 0.4, edgecolor='green',
                                         facecolor='lightgreen', linewidth=1.5)
            ax.add_patch(chloroplast)
        ax.text(7.5, 4.5, 'Chloroplasts', fontsize=10, style='italic')
        
        # Large vacuole
        vacuole = patches.Rectangle((1.5, 1.2), 1.5, 4, edgecolor='cyan',
                                   facecolor='lightcyan', linewidth=2, alpha=0.5)
        ax.add_patch(vacuole)
        ax.text(2.25, 3.2, 'Vacuole', ha='center', fontsize=9, rotation=90)
        
        # Mitochondria
        for x, y in [(5.5, 5.5), (6.5, 5)]:
            mito = patches.Ellipse((x, y), 0.5, 0.3, edgecolor='red',
                                  facecolor='pink', linewidth=1.5)
            ax.add_patch(mito)
        ax.text(6.5, 5.7, 'Mitochondria', fontsize=9, style='italic')
        
        ax.text(4.5, 0.3, 'Cell Wall', ha='center', fontsize=11, 
               fontweight='bold', color='darkgreen')
        
        title = 'Plant Cell Structure'
        
    else:  # animal cell
        # Animal cell - irregular oval shape
        cell_membrane = patches.Ellipse((4.5, 3.5), 7, 5, edgecolor='blue',
                                       facecolor='lightyellow', linewidth=3, alpha=0.3)
        ax.add_patch(cell_membrane)
        
        # Nucleus
        nucleus = patches.Circle((4.5, 3.5), 1, edgecolor='purple',
                                facecolor='lavender', linewidth=2)
        ax.add_patch(nucleus)
        ax.text(4.5, 3.5, 'Nucleus', ha='center', va='center', fontsize=10, fontweight='bold')
        
        # Mitochondria (multiple)
        for x, y in [(2.5, 2), (6.5, 2.5), (2, 4.5), (6.8, 4.5), (3.5, 5.5), (5.5, 1.8)]:
            mito = patches.Ellipse((x, y), 0.5, 0.3, edgecolor='red',
                                  facecolor='pink', linewidth=1.5)
            ax.add_patch(mito)
        ax.text(7.5, 4.5, 'Mitochondria', fontsize=10, style='italic')
        
        # Small vacuoles
        for x, y in [(2.2, 3), (3, 1.8), (6, 5.2)]:
            vac = patches.Circle((x, y), 0.15, edgecolor='cyan',
                                facecolor='lightcyan', linewidth=1)
            ax.add_patch(vac)
        ax.text(2.2, 2.5, 'Small\nVacuoles', ha='center', fontsize=8, style='italic')
        
        # Ribosomes (small dots)
        for x, y in [(3.2, 4.8), (5.8, 4.7), (3.8, 2.3), (5.2, 2.5), (4, 5.8)]:
            ax.plot(x, y, 'ko', markersize=3)
        ax.text(5.8, 5.8, 'Ribosomes', fontsize=9, style='italic')
        
        ax.text(4.5, 0.8, 'Cell Membrane', ha='center', fontsize=11,
               fontweight='bold', color='blue')
        
        title = 'Animal Cell Structure'
    
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 7)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
    
    filepath = DIAGRAMS_DIR / filename
    plt.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close()
    
    return str(filepath.absolute())


def plot_motion_graph(graph_type: str, values: List[Tuple[float, float]], 
                     labels: dict = None, filename: str = None) -> str:
    """
    Plot motion graphs (distance-time, velocity-time, acceleration-time)
    
    Args:
        graph_type: "distance-time", "velocity-time", or "acceleration-time"
        values: List of (time, value) tuples
        labels: Dict with 'title', 'xlabel', 'ylabel'
        filename: Optional custom filename
    
    Returns:
        Path to the saved diagram
    """
    if filename is None:
        filename = f"{graph_type.replace('-', '_')}_graph.png"
    
    times, vals = zip(*values) if values else ([], [])
    
    plt.figure(figsize=(10, 8))
    plt.plot(times, vals, 'b-', linewidth=2, marker='o', markersize=8)
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
    
    if labels:
        plt.title(labels.get('title', graph_type.replace('-', ' ').title()), 
                 fontsize=14, fontweight='bold')
        plt.xlabel(labels.get('xlabel', 'Time (s)'), fontsize=12)
        plt.ylabel(labels.get('ylabel', 'Value'), fontsize=12)
    else:
        plt.title(graph_type.replace('-', ' ').title(), fontsize=14, fontweight='bold')
        plt.xlabel('Time (s)', fontsize=12)
        
        if 'distance' in graph_type:
            plt.ylabel('Distance (m)', fontsize=12)
        elif 'velocity' in graph_type:
            plt.ylabel('Velocity (m/s)', fontsize=12)
        else:
            plt.ylabel('Acceleration (m/s²)', fontsize=12)
    
    filepath = DIAGRAMS_DIR / filename
    plt.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close()
    
    return str(filepath.absolute())


def draw_triangle(sides: List[float] = None, angles: List[float] = None,
                 triangle_type: str = None, filename: str = None) -> str:
    """
    Draw a triangle with given properties
    
    Args:
        sides: List of 3 side lengths
        angles: List of 3 angles (in degrees)
        triangle_type: "equilateral", "isosceles", "scalene", "right"
        filename: Optional custom filename
    
    Returns:
        Path to the saved diagram
    """
    if filename is None:
        filename = f"triangle_{triangle_type or 'custom'}.png"
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Default to equilateral if nothing specified
    if triangle_type == "equilateral" or (not sides and not angles):
        points = np.array([[0, 0], [4, 0], [2, 3.464]])
        sides = [4, 4, 4]
        angles = [60, 60, 60]
    elif triangle_type == "right":
        points = np.array([[0, 0], [4, 0], [0, 3]])
        sides = [4, 3, 5]
        angles = [90, 53.13, 36.87]
    elif triangle_type == "isosceles":
        points = np.array([[0, 0], [4, 0], [2, 3]])
        sides = [4, 3.16, 3.16]
        angles = [90, 45, 45]
    else:
        # Default scalene
        points = np.array([[0, 0], [5, 0], [2, 3]])
        sides = [5, 3.6, 3.16]
        angles = [59, 56, 65]
    
    # Draw triangle
    triangle = patches.Polygon(points, closed=True, edgecolor='blue',
                              facecolor='lightblue', linewidth=2, alpha=0.3)
    ax.add_patch(triangle)
    
    # Label vertices
    labels = ['A', 'B', 'C']
    offsets = [(-0.3, -0.3), (0.3, -0.3), (0, 0.3)]
    for i, (point, label, offset) in enumerate(zip(points, labels, offsets)):
        ax.plot(point[0], point[1], 'ro', markersize=8)
        ax.text(point[0] + offset[0], point[1] + offset[1], label,
               fontsize=14, fontweight='bold')
    
    # Label sides
    if sides:
        mid_points = [
            (points[0] + points[1]) / 2,
            (points[1] + points[2]) / 2,
            (points[2] + points[0]) / 2
        ]
        side_offsets = [(0, -0.5), (0.5, 0.3), (-0.5, 0.3)]
        for i, (mid, side, offset) in enumerate(zip(mid_points, sides, side_offsets)):
            ax.text(mid[0] + offset[0], mid[1] + offset[1], f'{side:.1f}',
                   fontsize=11, style='italic', color='darkblue')
    
    ax.set_xlim(-1, 6)
    ax.set_ylim(-1, 5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    title = f'{triangle_type.title() if triangle_type else "Triangle"}'
    ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
    
    filepath = DIAGRAMS_DIR / filename
    plt.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close()
    
    return str(filepath.absolute())


def get_tool_functions():
    """
    Get a dictionary mapping tool names to their functions
    
    Returns:
        Dict of tool name -> function
    """
    return {
        "plot_quadratic_function": plot_quadratic_function,
        "plot_linear_function": plot_linear_function,
        "draw_cell_diagram": draw_cell_diagram,
        "plot_motion_graph": plot_motion_graph,
        "draw_triangle": draw_triangle,
    }


# Tool definitions for the agent to use
DIAGRAM_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "plot_quadratic_function",
            "description": "Generate a visual graph of a quadratic function (parabola) showing the curve, vertex, and roots. Use this when explaining quadratic equations, parabolas, or solving x² equations.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "Coefficient of x² term (e.g., 1 for x², 2 for 2x²)"
                    },
                    "b": {
                        "type": "number",
                        "description": "Coefficient of x term (e.g., -5 for -5x)"
                    },
                    "c": {
                        "type": "number",
                        "description": "Constant term (e.g., 6 for +6)"
                    }
                },
                "required": ["a", "b", "c"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "plot_linear_function",
            "description": "Generate a visual graph of a linear function (straight line) showing the line, slope, and intercepts. Use when explaining linear equations, slopes, or y = mx + c.",
            "parameters": {
                "type": "object",
                "properties": {
                    "m": {
                        "type": "number",
                        "description": "Slope of the line (rise/run)"
                    },
                    "c": {
                        "type": "number",
                        "description": "Y-intercept (where line crosses y-axis)"
                    }
                },
                "required": ["m", "c"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "draw_cell_diagram",
            "description": "Generate a labeled diagram of a plant or animal cell showing all major organelles. Use when explaining cell structure, organelles, or differences between plant and animal cells.",
            "parameters": {
                "type": "object",
                "properties": {
                    "cell_type": {
                        "type": "string",
                        "enum": ["plant", "animal"],
                        "description": "Type of cell to draw: 'plant' or 'animal'"
                    }
                },
                "required": ["cell_type"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "plot_motion_graph",
            "description": "Generate physics motion graphs (distance-time, velocity-time, or acceleration-time). Use when explaining motion, speed, velocity, or acceleration concepts.",
            "parameters": {
                "type": "object",
                "properties": {
                    "graph_type": {
                        "type": "string",
                        "enum": ["distance-time", "velocity-time", "acceleration-time"],
                        "description": "Type of motion graph"
                    },
                    "values": {
                        "type": "array",
                        "description": "Array of [time, value] pairs, e.g., [[0, 0], [2, 10], [4, 20]]",
                        "items": {
                            "type": "array",
                            "items": {"type": "number"}
                        }
                    }
                },
                "required": ["graph_type", "values"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "draw_triangle",
            "description": "Generate a labeled triangle diagram. Use when explaining geometry, types of triangles, or triangle properties.",
            "parameters": {
                "type": "object",
                "properties": {
                    "triangle_type": {
                        "type": "string",
                        "enum": ["equilateral", "isosceles", "scalene", "right"],
                        "description": "Type of triangle to draw"
                    }
                },
                "required": ["triangle_type"]
            }
        }
    }
]

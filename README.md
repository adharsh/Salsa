# Salsa

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME/main)

## Overview

Salsa is a project that generates and visualizes social network graphs using dot files.

![Sample Graph](path/to/sample_graph_image.png)

## Using Binder

Click on the Binder badge above to launch an interactive environment where you can run the Salsa project without any local setup.

## Working with Dot Files

### Generating the Social Network Graph

To generate the `social_all_dile_que_no_is_same.dot` file, run:

```bash
./all_dile_que_no_is_same.sh
```

### Visualizing Dot Files with xdot

To visualize the generated dot files using xdot, follow these steps:

1. Install xdot if you haven't already:
   ```bash
   sudo apt-get install xdot
   ```

2. Open a dot file with xdot:
   ```bash
   xdot social_all_dile_que_no_is_same.dot
   ```

3. Use the mouse to navigate the graph:
   - Scroll to zoom in/out
   - Click and drag to pan
   - Double-click a node to center it

## Sample Visualizations

Here are some sample visualizations generated from our dot files:

![Visualization 1](path/to/visualization1.png)
![Visualization 2](path/to/visualization2.png)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).

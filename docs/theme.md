# Theming Guide

Infra Manager Studio embraces a hacker inspired aesthetic with dark neutrals and
blood red highlights. Themes are defined in `ui/theme.py`.

## Default Palette

| Element            | Color    |
| ------------------ | -------- |
| Background         | `#111111`|
| Accent             | `#8A0303`|
| Text               | `#E4E4E4`|
| Card Background    | `#1F1F1F`|

Adjust the palette by modifying `Theme.default()`. For custom backgrounds use
`Theme.with_background(path)`.

## Applying Themes

- `InfraManagerApplication` sets the application palette and stylesheet on
  startup.
- Toolbars, cards, and dialogs inherit the palette automatically.
- The "Toggle Neon" toolbar button swaps the accent color and animates the
  background for extra flair.

## Background Images

Call `main("/path/to/background.png")` or choose "Set Background" from the
toolbar to layer an image behind the UI. Images are scaled to cover the window.

## Animation Tips

Use `QPropertyAnimation` and `QVariantAnimation` for smooth transitions. The
startup fade effect in `MainWindow._animate_startup` can be reused for other
widgets to create staged entrances.

New operations panels lean on `QTreeWidget`, `QTableWidget`, and `QProgressBar`
controls. Apply consistent styling by extending the stylesheet in `Theme.apply`
to cover `QTreeView`, `QHeaderView::section`, and `QProgressBar` selectors so the
cron, async job, and batch views remain on-brand.

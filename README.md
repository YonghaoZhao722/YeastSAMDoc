# AutoOutline 文档网站

这是 AutoOutline 的文档网站，使用 MkDocs 构建并部署在 GitHub Pages 上。

## 本地开发

要在本地运行此文档网站，请按照以下步骤操作：

1. 克隆此仓库
   ```
   git clone <repository-url>
   cd <repository-name>
   ```

2. 安装依赖
   ```
   pip install -r requirements.txt
   ```

3. 本地预览
   ```
   mkdocs serve
   ```
   然后在浏览器中打开 http://localhost:8000

## 部署到 GitHub Pages

要将网站部署到 GitHub Pages，请运行：

```
mkdocs gh-deploy
```

## 目录结构

- `docs/` - 所有文档的 Markdown 文件
- `mkdocs.yml` - MkDocs 配置文件

## 贡献指南

如果您想贡献内容或修复，请提交 Pull Request。 
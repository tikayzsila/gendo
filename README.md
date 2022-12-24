# Утилита для генерации конфигов

Простая утилита для создания ci и docker конфигов и ansible роли

## Установка

Для установки нужен poetry (pip install poetry или через скрипт как в оф. гайде)
После установки poetry достаточно прописать make install и установятся необходимые библиотеки и сама утилита

## Использование

Для использования нужны все темплейты с папки templates, А также я yaml конфиг(gendo.yml):
      ---
      lang: python
      project_name: web

      compose:
        port_host: 8888

      gitlab-ci:
        branch: ci/test
        gitlab_templates_repo: ivanov_vs/ci-templates

      ansible:
        staging_ip: 192.168.1.1
        prod_ip: 127.0.0.1

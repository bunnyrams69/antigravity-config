# Standalone Stack Boilerplates (screenshot-to-code)

Use these proven, standalone boilerplate templates to produce self-contained, immediately runnable HTML files from screenshots.

---

## 1. HTML + Tailwind CSS (Recommended Default)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Generated Preview</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Inter', sans-serif; }
  </style>
</head>
<body class="bg-gray-50 text-gray-900 antialiased">
  <!-- Replicated UI Content Goes Here -->
</body>
</html>
```

---

## 2. React + Tailwind CSS (Standalone)

> **IMPORTANT**: Always use Babel Standalone 7.25.6 (`https://unpkg.com/@babel/standalone@7.25.6/babel.min.js`). Unversioned Babel resolves to Babel 8 which breaks browser runtime JSX transforms.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>React Preview</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <script src="https://cdn.jsdelivr.net/npm/react@18.0.0/umd/react.development.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/react-dom@18.0.0/umd/react-dom.development.js"></script>
  <script src="https://unpkg.com/@babel/standalone@7.25.6/babel.min.js"></script>
</head>
<body class="bg-gray-50 text-gray-900">
  <div id="root"></div>

  <script type="text/babel">
    const { useState, useEffect } = React;

    function App() {
      return (
        <div className="min-h-screen">
          {/* Replicated UI Content Goes Here */}
        </div>
      );
    }

    const root = ReactDOM.createRoot(document.getElementById('root'));
    root.render(<App />);
  </script>
</body>
</html>
```

---

## 3. Vue 3 + Tailwind CSS (Standalone)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vue Preview</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body class="bg-gray-50 text-gray-900">
  <div id="app">
    <!-- Replicated UI with Vue bindings -->
  </div>

  <script>
    const { createApp, ref } = Vue;
    createApp({
      setup() {
        return {};
      }
    }).mount('#app');
  </script>
</body>
</html>
```

---

## 4. Ionic + Tailwind CSS (Mobile Apps)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ionic Mobile Preview</title>
  <script type="module" src="https://cdn.jsdelivr.net/npm/@ionic/core/dist/ionic/ionic.esm.js"></script>
  <script nomodule src="https://cdn.jsdelivr.net/npm/@ionic/core/dist/ionic/ionic.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@ionic/core/css/ionic.bundle.css" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <ion-app>
    <!-- Ionic components (ion-header, ion-toolbar, ion-content, ion-card, etc.) -->
  </ion-app>

  <script type="module" src="https://cdn.jsdelivr.net/npm/ionicons/+esm"></script>
  <script nomodule src="https://cdn.jsdelivr.net/npm/ionicons/dist/esm/ionicons.min.js"></script>
</body>
</html>
```

---

## 5. Bootstrap 5.3

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bootstrap Preview</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
</head>
<body>
  <!-- Bootstrap components -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

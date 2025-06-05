{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "adb28785",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "A module that was compiled using NumPy 1.x cannot be run in\n",
      "NumPy 2.0.2 as it may crash. To support both 1.x and 2.x\n",
      "versions of NumPy, modules must be compiled with NumPy 2.0.\n",
      "Some module may need to rebuild instead e.g. with 'pybind11>=2.12'.\n",
      "\n",
      "If you are a user of the module, the easiest solution will be to\n",
      "downgrade to 'numpy<2' or try to upgrade the affected module.\n",
      "We expect that some modules will need time to support NumPy 2.\n",
      "\n",
      "Traceback (most recent call last):  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\runpy.py\", line 197, in _run_module_as_main\n",
      "    return _run_code(code, main_globals, None,\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\runpy.py\", line 87, in _run_code\n",
      "    exec(code, run_globals)\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\ipykernel_launcher.py\", line 16, in <module>\n",
      "    app.launch_new_instance()\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\traitlets\\config\\application.py\", line 846, in launch_instance\n",
      "    app.start()\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\ipykernel\\kernelapp.py\", line 677, in start\n",
      "    self.io_loop.start()\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\tornado\\platform\\asyncio.py\", line 199, in start\n",
      "    self.asyncio_loop.run_forever()\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\asyncio\\base_events.py\", line 601, in run_forever\n",
      "    self._run_once()\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\asyncio\\base_events.py\", line 1905, in _run_once\n",
      "    handle._run()\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\asyncio\\events.py\", line 80, in _run\n",
      "    self._context.run(self._callback, *self._args)\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py\", line 471, in dispatch_queue\n",
      "    await self.process_one()\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py\", line 460, in process_one\n",
      "    await dispatch(*args)\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py\", line 367, in dispatch_shell\n",
      "    await result\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py\", line 662, in execute_request\n",
      "    reply_content = await reply_content\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\ipykernel\\ipkernel.py\", line 360, in do_execute\n",
      "    res = shell.run_cell(code, store_history=store_history, silent=silent)\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\ipykernel\\zmqshell.py\", line 532, in run_cell\n",
      "    return super().run_cell(*args, **kwargs)\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py\", line 2863, in run_cell\n",
      "    result = self._run_cell(\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py\", line 2909, in _run_cell\n",
      "    return runner(coro)\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\IPython\\core\\async_helpers.py\", line 129, in _pseudo_sync_runner\n",
      "    coro.send(None)\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py\", line 3106, in run_cell_async\n",
      "    has_raised = await self.run_ast_nodes(code_ast.body, cell_name,\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py\", line 3309, in run_ast_nodes\n",
      "    if await self.run_code(code, result, async_=asy):\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py\", line 3369, in run_code\n",
      "    exec(code_obj, self.user_global_ns, self.user_ns)\n",
      "  File \"C:\\conda_tmp\\ipykernel_3064\\256561234.py\", line 3, in <cell line: 3>\n",
      "    import folium\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\folium\\__init__.py\", line 15, in <module>\n",
      "    from folium.features import (\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\folium\\features.py\", line 37, in <module>\n",
      "    from folium.elements import JSCSSMixin\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\folium\\elements.py\", line 11, in <module>\n",
      "    from folium.template import Template\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\folium\\template.py\", line 7, in <module>\n",
      "    from folium.utilities import JsCode, TypeJsonValue, camelize\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\folium\\utilities.py\", line 41, in <module>\n",
      "    import pandas as pd\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\pandas\\__init__.py\", line 80, in <module>\n",
      "    from pandas.core.api import (\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\pandas\\core\\api.py\", line 28, in <module>\n",
      "    from pandas.core.arrays import Categorical\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\pandas\\core\\arrays\\__init__.py\", line 1, in <module>\n",
      "    from pandas.core.arrays.arrow import ArrowExtensionArray\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\pandas\\core\\arrays\\arrow\\__init__.py\", line 5, in <module>\n",
      "    from pandas.core.arrays.arrow.array import ArrowExtensionArray\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\pandas\\core\\arrays\\arrow\\array.py\", line 50, in <module>\n",
      "    from pandas.core import (\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\pandas\\core\\ops\\__init__.py\", line 8, in <module>\n",
      "    from pandas.core.ops.array_ops import (\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\pandas\\core\\ops\\array_ops.py\", line 56, in <module>\n",
      "    from pandas.core.computation import expressions\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\pandas\\core\\computation\\expressions.py\", line 21, in <module>\n",
      "    from pandas.core.computation.check import NUMEXPR_INSTALLED\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\pandas\\core\\computation\\check.py\", line 5, in <module>\n",
      "    ne = import_optional_dependency(\"numexpr\", errors=\"warn\")\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\pandas\\compat\\_optional.py\", line 135, in import_optional_dependency\n",
      "    module = importlib.import_module(name)\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\importlib\\__init__.py\", line 127, in import_module\n",
      "    return _bootstrap._gcd_import(name[level:], package, level)\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\numexpr\\__init__.py\", line 24, in <module>\n",
      "    from numexpr.interpreter import MAX_THREADS, use_vml, __BLOCK_SIZE1__\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "_ARRAY_API not found",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;31mAttributeError\u001b[0m: _ARRAY_API not found"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "A module that was compiled using NumPy 1.x cannot be run in\n",
      "NumPy 2.0.2 as it may crash. To support both 1.x and 2.x\n",
      "versions of NumPy, modules must be compiled with NumPy 2.0.\n",
      "Some module may need to rebuild instead e.g. with 'pybind11>=2.12'.\n",
      "\n",
      "If you are a user of the module, the easiest solution will be to\n",
      "downgrade to 'numpy<2' or try to upgrade the affected module.\n",
      "We expect that some modules will need time to support NumPy 2.\n",
      "\n",
      "Traceback (most recent call last):  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\runpy.py\", line 197, in _run_module_as_main\n",
      "    return _run_code(code, main_globals, None,\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\runpy.py\", line 87, in _run_code\n",
      "    exec(code, run_globals)\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\ipykernel_launcher.py\", line 16, in <module>\n",
      "    app.launch_new_instance()\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\traitlets\\config\\application.py\", line 846, in launch_instance\n",
      "    app.start()\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\ipykernel\\kernelapp.py\", line 677, in start\n",
      "    self.io_loop.start()\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\tornado\\platform\\asyncio.py\", line 199, in start\n",
      "    self.asyncio_loop.run_forever()\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\asyncio\\base_events.py\", line 601, in run_forever\n",
      "    self._run_once()\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\asyncio\\base_events.py\", line 1905, in _run_once\n",
      "    handle._run()\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\asyncio\\events.py\", line 80, in _run\n",
      "    self._context.run(self._callback, *self._args)\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py\", line 471, in dispatch_queue\n",
      "    await self.process_one()\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py\", line 460, in process_one\n",
      "    await dispatch(*args)\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py\", line 367, in dispatch_shell\n",
      "    await result\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py\", line 662, in execute_request\n",
      "    reply_content = await reply_content\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\ipykernel\\ipkernel.py\", line 360, in do_execute\n",
      "    res = shell.run_cell(code, store_history=store_history, silent=silent)\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\ipykernel\\zmqshell.py\", line 532, in run_cell\n",
      "    return super().run_cell(*args, **kwargs)\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py\", line 2863, in run_cell\n",
      "    result = self._run_cell(\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py\", line 2909, in _run_cell\n",
      "    return runner(coro)\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\IPython\\core\\async_helpers.py\", line 129, in _pseudo_sync_runner\n",
      "    coro.send(None)\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py\", line 3106, in run_cell_async\n",
      "    has_raised = await self.run_ast_nodes(code_ast.body, cell_name,\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py\", line 3309, in run_ast_nodes\n",
      "    if await self.run_code(code, result, async_=asy):\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py\", line 3369, in run_code\n",
      "    exec(code_obj, self.user_global_ns, self.user_ns)\n",
      "  File \"C:\\conda_tmp\\ipykernel_3064\\256561234.py\", line 3, in <cell line: 3>\n",
      "    import folium\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\folium\\__init__.py\", line 15, in <module>\n",
      "    from folium.features import (\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\folium\\features.py\", line 37, in <module>\n",
      "    from folium.elements import JSCSSMixin\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\folium\\elements.py\", line 11, in <module>\n",
      "    from folium.template import Template\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\folium\\template.py\", line 7, in <module>\n",
      "    from folium.utilities import JsCode, TypeJsonValue, camelize\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\folium\\utilities.py\", line 41, in <module>\n",
      "    import pandas as pd\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\pandas\\__init__.py\", line 80, in <module>\n",
      "    from pandas.core.api import (\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\pandas\\core\\api.py\", line 28, in <module>\n",
      "    from pandas.core.arrays import Categorical\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\pandas\\core\\arrays\\__init__.py\", line 1, in <module>\n",
      "    from pandas.core.arrays.arrow import ArrowExtensionArray\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\pandas\\core\\arrays\\arrow\\__init__.py\", line 5, in <module>\n",
      "    from pandas.core.arrays.arrow.array import ArrowExtensionArray\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\pandas\\core\\arrays\\arrow\\array.py\", line 64, in <module>\n",
      "    from pandas.core.arrays.masked import BaseMaskedArray\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\pandas\\core\\arrays\\masked.py\", line 60, in <module>\n",
      "    from pandas.core import (\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\pandas\\core\\nanops.py\", line 52, in <module>\n",
      "    bn = import_optional_dependency(\"bottleneck\", errors=\"warn\")\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\pandas\\compat\\_optional.py\", line 135, in import_optional_dependency\n",
      "    module = importlib.import_module(name)\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\importlib\\__init__.py\", line 127, in import_module\n",
      "    return _bootstrap._gcd_import(name[level:], package, level)\n",
      "  File \"C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\bottleneck\\__init__.py\", line 7, in <module>\n",
      "    from .move import (move_argmax, move_argmin, move_max, move_mean, move_median,\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "_ARRAY_API not found",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;31mAttributeError\u001b[0m: _ARRAY_API not found"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-05 11:22:50.990 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import openrouteservice\n",
    "import folium\n",
    "from streamlit_folium import st_folium"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "def63cdd",
   "metadata": {},
   "outputs": [],
   "source": [
    "client = openrouteservice.Client(key=\"5b3ce3597851110001cf6248fd384fc7d57149b19033e37efb7e90ec\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2dec9975",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-05 11:24:11.545 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-05 11:24:12.077 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Mayur Gharate\\anaconda3\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-06-05 11:24:12.078 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-05 11:24:12.078 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-05 11:24:12.078 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "locations_dict = {\n",
    "    \"Chennai\":        [80.2707, 13.0827],\n",
    "    \"Bengaluru\":      [77.5946, 12.9716],\n",
    "    \"Hyderabad\":      [78.4867, 17.3850],\n",
    "    \"Coimbatore\":     [76.9558, 11.0168],\n",
    "    \"Mumbai\":         [72.8777, 19.0760],\n",
    "    \"Pune\":           [73.8567, 18.5204],\n",
    "    \"Ahmedabad\":      [72.5714, 23.0225],\n",
    "    \"Nagpur\":         [79.0882, 21.1458],\n",
    "    \"Kolkata\":        [88.3639, 22.5726],\n",
    "    \"Visakhapatnam\":  [83.2185, 17.6868],\n",
    "}\n",
    "\n",
    "st.title(\"🧭 Route Optimization Tool\")\n",
    "st.subheader(\"Select Locations to Visit:\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "fe0174cc",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-05 11:25:27.505 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-05 11:25:27.507 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-05 11:25:27.509 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-05 11:25:27.511 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-05 11:25:27.512 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "selected_locations = st.multiselect(\n",
    "    \"Choose locations in the order you'd like to visit (min 2):\",\n",
    "    list(locations_dict.keys())\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "6936993c",
   "metadata": {},
   "outputs": [],
   "source": [
    "if len(selected_locations) >= 2:\n",
    "    coordinates = [locations_dict[loc] for loc in selected_locations]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "82062474",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-05 11:27:51.001 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-05 11:27:51.003 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "    try:\n",
    "        optimized = client.directions(\n",
    "            coordinates=coordinates,\n",
    "            profile='driving-car',\n",
    "            optimize_waypoints=True,\n",
    "            format='geojson'\n",
    "        )\n",
    "\n",
    "        # Create map\n",
    "        m = folium.Map(location=coordinates[0][::-1], zoom_start=6)\n",
    "        folium.GeoJson(optimized).add_to(m)\n",
    "\n",
    "        for loc in selected_locations:\n",
    "            folium.Marker(locations_dict[loc][::-1], popup=loc).add_to(m)\n",
    "\n",
    "        st.success(\"✅ Optimized route generated below:\")\n",
    "        st_folium(m, width=725)\n",
    "\n",
    "    except Exception as e:\n",
    "        st.error(f\"Error during optimization: {e}\")\n",
    "else:\n",
    "     st.warning(\"Please select at least two locations to proceed.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "45b8dddc",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "c9b3bd79",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

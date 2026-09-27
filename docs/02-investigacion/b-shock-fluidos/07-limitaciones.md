# 07 · Limitaciones y errores

La ecografía en el shock es potente, pero **cada medida tiene condiciones de validez**. Fuera de ellas da falsos positivos y falsos negativos que pueden llevar a dar fluidos a quien no los tolera o a negárselos a quien los necesita. Esta página recoge las limitaciones de cada herramienta: VCI, VTI, EPP, VExUS y FoCUS en manos no expertas. También trata la dependencia del operador, los errores cognitivos más frecuentes, el shock mixto y los límites de los protocolos como el RUSH. La técnica correcta está en [02 · Técnica](02-tecnica.md), la precisión diagnóstica en [03 · Precisión](03-precision.md) y la formación necesaria en [08 · Formación](08-formacion.md).

!!! abstract "Regla general"
    Un hallazgo ecográfico es un **dato fisiológico que hay que interpretar en su contexto**, no un diagnóstico. La mayoría de los errores se evitan siguiendo unas reglas de técnica e interpretación e integrando siempre la ecografía en el cuadro clínico ([Blanco, 2016](../../05-fuentes/index.md#blanco2016)).

## Vena cava inferior

La VCI es la medida más popular y la más discutida. Su diámetro y su variación respiratoria no dependen solo del volumen. También influyen la distensibilidad de la propia vena, la presión extramural (la presión intraabdominal) y cómo se transmite la presión intratorácica al abdomen ([Monnet, 2022](../../05-fuentes/index.md#monnet2022)). Por eso Monnet y colaboradores se sorprenden de que la distensibilidad de la VCI se considere a menudo el índice clave para valorar las necesidades de fluidos en POCUS ([Monnet, 2022](../../05-fuentes/index.md#monnet2022)).

### Ventilación mecánica frente a respiración espontánea

| Situación | Qué ocurre con la VCI | Consecuencia | Fuente |
|---|---|---|---|
| **Ventilación mecánica controlada**, sedación, sin esfuerzo | La VCI se **distiende** en la inspiración por la presión positiva | Se usa la **distensibilidad**. Rendimiento aceptable, aunque inferior a la VPP o la VVS (AUC 0,83 frente a 0,87) | [Chaves, 2024](../../05-fuentes/index.md#chaves2024) |
| **Esfuerzos inspiratorios** en el paciente ventilado | Mezcla de distensión pasiva y colapso activo | La distensibilidad solo es válida **sin esfuerzos espontáneos** (LR+ 5,3 en ese subgrupo) | [Bentzer, 2016](../../05-fuentes/index.md#bentzer2016) |
| **Volumen corriente bajo** o **distensibilidad pulmonar baja** | Poca transmisión de presión a la VCI | **Falsos negativos** | [Monnet, 2022](../../05-fuentes/index.md#monnet2022) |
| **Respiración espontánea** | La VCI **colapsa** en la inspiración | Se usa la **colapsabilidad**: S 63 % y E 83 %, con mucha clasificación errónea. No usar de forma aislada | [Cardozo Júnior, 2023](../../05-fuentes/index.md#cardozo2023) |
| **Esfuerzo respiratorio variable** (disnea, respiración superficial o forzada) | El colapso depende de la **intensidad de la inspiración**, no solo de la volemia | Sin estandarizar, la precisión cae (AUC 0,85 frente a 0,98) | [Caplan, 2020](../../05-fuentes/index.md#caplan2020) |
| **Espiración activa** o paciente que no colabora | No se puede estandarizar la maniobra | La colapsabilidad no es interpretable | [Monnet, 2022](../../05-fuentes/index.md#monnet2022) |

!!! warning "Error frecuente"
    Interpretar como «hipovolemia» una VCI que colapsa mucho en un paciente **taquipneico con gran esfuerzo inspiratorio**. Un esfuerzo intenso puede colapsar una VCI incluso con una presión venosa normal o alta. En respiración espontánea hay que **estandarizar la inspiración** ([Preau, 2017](../../05-fuentes/index.md#preau2017); [Caplan, 2020](../../05-fuentes/index.md#caplan2020)) o, mejor, pasar a una medida de flujo como la **EPP con VTI**.

### Presión intraabdominal elevada

- La **hipertensión intraabdominal** puede **colapsar la VCI pese a una PAD elevada** ([Assavapokee, 2024](../../05-fuentes/index.md#assavapokee2024)).
- El valor diagnóstico de la variación de la VCI se vuelve **muy bajo** con hipertensión intraabdominal ([Monnet, 2022](../../05-fuentes/index.md#monnet2022)).
- Es un problema frecuente en los pacientes con sobrecarga: el balance positivo se asocia a la hipertensión intraabdominal ([Malbrain, 2014](../../05-fuentes/index.md#malbrain2014)).

### Disfunción del VD, insuficiencia tricuspídea y otras causas de VCI «pletórica»

La relación entre el tamaño de la VCI y la volemia falla en muchas situaciones ([Blanco, 2016](../../05-fuentes/index.md#blanco2016)):

- infarto del VD, taponamiento y TEP masivo, en los que la VCI está dilatada aunque el paciente pueda necesitar precarga;
- *cor pulmonale* agudo o crónico, **insuficiencia tricuspídea grave** y constricción pericárdica, con una dinámica de la VCI muy variable e independiente de la volemia;
- asma o EPOC agudizadas y ventilación con presión positiva;
- presiones de llenado izquierdas altas con VCI normal;
- pacientes que responden a fluidos con una VCI **fisiológicamente dilatada**.

La ASE/BSE recoge otro matiz: la categoría intermedia de PAD se reclasifica según índices secundarios (llenado restrictivo del VD, E/e′ tricuspídeo > 6, flujo diastólico invertido en las suprahepáticas) ([Zaidi, 2020](../../05-fuentes/index.md#zaidi2020)).

!!! warning "Error frecuente"
    Ver una VCI grande y no colapsable y concluir que el paciente está «lleno» y no necesita fluidos, o incluso darle diuréticos. En el infarto del VD o en el shock obstructivo, el paciente puede necesitar precarga. Y, al revés, el error de la VCI puede llevar a dar fluidos a pacientes con presiones izquierdas altas y producir congestión pulmonar ([Blanco, 2016](../../05-fuentes/index.md#blanco2016)).

### Errores técnicos de medida

| Error | Mecanismo | Cómo evitarlo | Fuente |
|---|---|---|---|
| **Traslación de la VCI** | En la inspiración la vena se desplaza en sentido craneocaudal o lateral y sale del plano o del cursor del modo M, **simulando un colapso** | Comprobar el modo M con el 2D simultáneo y seguir la vena durante todo el ciclo | [Blanco, 2016](../../05-fuentes/index.md#blanco2016) |
| **Efecto cilindro** | Un corte tangencial en eje largo infraestima el diámetro | Confirmar en eje corto (VCI circular o aplanada) | [Assavapokee, 2024](../../05-fuentes/index.md#assavapokee2024) |
| **Punto de medida** | El colapso varía a lo largo de la vena: es menor junto al diafragma | Medir de forma estandarizada. Para la respuesta en respiración espontánea, a ≈ 4 cm de la AD; no en la unión cavoatrial | [Wallace, 2010](../../05-fuentes/index.md#wallace2010); [Caplan, 2020](../../05-fuentes/index.md#caplan2020) |
| **Confundir la VCI con la aorta** | Ambas pueden latir: la VCI lo hace en los estados hiperdinámicos y en la insuficiencia tricuspídea | La aorta está en la línea media, separada del hígado y con ramas anteriores | [Assavapokee, 2024](../../05-fuentes/index.md#assavapokee2024) |
| **Modo M poco reproducible** | Pequeños cambios de ángulo alteran los diámetros | El modo B en eje largo es el más reproducible (CCI 0,86). Los índices de colapso con modo M son los menos fiables | [Finnerty, 2017](../../05-fuentes/index.md#finnerty2017) |
| **Ventana subcostal no disponible** (obesidad, gas, cirugía abdominal, apósitos) | No se ve la VCI | Vista coronal transhepática (*rescue view*) | [Finnerty, 2017](../../05-fuentes/index.md#finnerty2017); [Saul, 2012](../../05-fuentes/index.md#saul2012) |

### Variantes fisiológicas

- **Deportistas de resistencia:** la **VCI dilatada** es un hallazgo frecuente en deportistas de élite, sin elevación de la PAD ([Goldhammer, 1999](../../05-fuentes/index.md#goldhammer1999); [Assavapokee, 2024](../../05-fuentes/index.md#assavapokee2024)).
- **VCI pequeña en jóvenes sanos o personas delgadas:** se describe con frecuencia en la docencia como posible falso positivo de «hipovolemia», pero no se ha localizado un estudio que lo cuantifique `[POR VERIFICAR]`.
- **Poblaciones no occidentales:** el umbral de 2 cm puede requerir ajustes ([Assavapokee, 2024](../../05-fuentes/index.md#assavapokee2024)).

### Evidencia global sobre la VCI

- En el metaanálisis de 20 estudios, el índice de la VCI tuvo un AUC de 0,71, una sensibilidad del 71 % y una especificidad del 75 %, con **heterogeneidad extrema**. Los autores concluyen que no es un método fiable para predecir la respuesta a fluidos ([Orso, 2020](../../05-fuentes/index.md#orso2020)).
- La guía de ecocardiografía usa la VCI para **estimar la PAD**, que es otra pregunta ([Zaidi, 2020](../../05-fuentes/index.md#zaidi2020)). En la valoración de la congestión, la VCI aislada tampoco demuestra la congestión de los órganos ([Koratala, 2022](../../05-fuentes/index.md#koratala2022)).
- Hoy se propone reorientar la VCI **de la respuesta a la tolerancia**: una VCI pletórica sería una señal de alarma frente a más volumen ([Rola, 2024](../../05-fuentes/index.md#rola2024)). Es una propuesta de expertos.

## Integral velocidad-tiempo (VTI)

| Limitación | Detalle | Fuente |
|---|---|---|
| **Ángulo de insonación** | La VTI se infraestima si el haz no está alineado con el flujo del TSVI. Hay que buscar la alineación paralela y una envolvente con mínimo ensanchamiento espectral | [Blanco, 2020](../../05-fuentes/index.md#blanco2020) |
| **Ventana apical no disponible** | La apical se obtuvo en el 80 % de los pacientes de UCI; es más difícil en los pacientes ventilados, obesos o con EPOC | [Jensen, 2004](../../05-fuentes/index.md#jensen2004) |
| **Posición del volumen de muestra** | Cambiarla entre mediciones altera la VTI. Se coloca a ≈ 1 cm de la válvula aórtica | [Blanco, 2020](../../05-fuentes/index.md#blanco2020) |
| **Arritmias** (FA, extrasístoles) | Los distintos tiempos de llenado producen variabilidad latido a latido. Hay que promediar **al menos 5 latidos** | [Blanco, 2020](../../05-fuentes/index.md#blanco2020); [Jozwiak, 2019](../../05-fuentes/index.md#jozwiak2019) |
| **Precisión y reproducibilidad** | Cambio mínimo significativo del **11 %** con el mismo operador y del **14 %** con dos operadores | [Jozwiak, 2019](../../05-fuentes/index.md#jozwiak2019) |
| **Cálculo del volumen sistólico absoluto** | El error al medir el diámetro del TSVI se eleva al cuadrado: 2 mm de diferencia (1,8 frente a 2,0 cm) cambian el volumen sistólico un 26 % | [Blanco, 2020](../../05-fuentes/index.md#blanco2020) |
| **Insuficiencia aórtica y obstrucción dinámica del TSVI** | Señal con *aliasing* en la insuficiencia aórtica. En la obstrucción dinámica (hipovolemia grave, estados hiperdinámicos) aparecen velocidades altas con pico tardío y hay que usar Doppler continuo | [Blanco, 2020](../../05-fuentes/index.md#blanco2020) |

!!! tip "Perla clínica"
    Para comparar un antes y un después (EPP, bolo), **no hace falta calcular el volumen sistólico**: basta con la VTI. Lo que sí hace falta es que sea **el mismo operador, la misma ventana y la misma posición del volumen de muestra**, con 3 latidos promediados (5 en FA) ([Blanco, 2020](../../05-fuentes/index.md#blanco2020); [Jozwiak, 2019](../../05-fuentes/index.md#jozwiak2019)).

!!! warning "El mini-bolo y los umbrales pequeños"
    El umbral óptimo del mini-bolo en el metaanálisis fue del **5 %** ([Messina, 2019](../../05-fuentes/index.md#messina2019)), menos de la mitad del cambio mínimo que la ecocardiografía detecta de forma fiable (11 %) ([Jozwiak, 2019](../../05-fuentes/index.md#jozwiak2019)). Un aumento de la VTI del 5–10 % tras un mini-bolo **puede ser ruido de medida**.

## Elevación pasiva de piernas

| Limitación | Efecto | Fuente |
|---|---|---|
| **Hipertensión intraabdominal** | **Falsos negativos**. Con una PIA ≥ 16 mmHg, 15 de 31 pacientes que sí respondían a fluidos no respondieron a la EPP (n = 41, Doppler esofágico) | [Mahjoub, 2010](../../05-fuentes/index.md#mahjoub2010) |
| Hipertensión intraabdominal (confirmación) | 60 pacientes. Con hipertensión intraabdominal, la EPP fue negativa en 15 de 21 respondedores y su AUC cayó de 0,98 a **0,60** | [Beurton, 2019](../../05-fuentes/index.md#beurton2019) |
| **Hipertensión intracraneal** | **Contraindicación**, por el descenso de la cabeza | [Monnet, 2022](../../05-fuentes/index.md#monnet2022) |
| **Medias de compresión venosa** | Probables falsos negativos, porque se moviliza menos volumen | [Monnet, 2022](../../05-fuentes/index.md#monnet2022) |
| **Dolor, tos, incomodidad, despertar** | La estimulación adrenérgica produce **falsos positivos**. Se sospecha si la FC sube durante la prueba | [Monnet, 2015](../../05-fuentes/index.md#monnet2015) |
| **Empezar en decúbito supino** | Se moviliza menos volumen (sin el componente esplácnico) y la prueba pierde sensibilidad | [Monnet, 2015](../../05-fuentes/index.md#monnet2015) |
| **Medir la presión arterial en lugar del flujo** | Rendimiento mucho menor: la presión de pulso tiene una sensibilidad del 56 %, frente al 85 % del gasto | [Monnet, 2016](../../05-fuentes/index.md#monnet2016) |
| **Medir demasiado tarde** | El efecto puede desaparecer después de 1 minuto | [Monnet, 2015](../../05-fuentes/index.md#monnet2015) |
| **Amputación de miembros inferiores, fracturas de pelvis o de las extremidades inferiores, cirugía** | Menor volumen movilizado o imposibilidad de hacer la maniobra. En estos casos, alternativa: mini-bolo | Razonamiento fisiológico; no se han localizado estudios específicos `[POR VERIFICAR]`. La dificultad durante la cirugía sí está descrita en [Monnet, 2022](../../05-fuentes/index.md#monnet2022) |
| **Situaciones en que sigue siendo válida** | Respiración espontánea, arritmias, volumen corriente bajo, baja distensibilidad pulmonar, insuficiencia cardiaca derecha | [Monnet, 2022](../../05-fuentes/index.md#monnet2022) |

!!! note "Controversia"
    En 2015, Monnet y Teboul consideraban que la evidencia sobre la hipertensión intraabdominal era débil, porque el único estudio no midió la presión intraabdominal durante la EPP ([Monnet, 2015](../../05-fuentes/index.md#monnet2015)). En 2019, un estudio con medida directa confirmó los falsos negativos ([Beurton, 2019](../../05-fuentes/index.md#beurton2019)). Hoy se aconseja **cautela al interpretar una EPP negativa con hipertensión intraabdominal** ([Monnet, 2022](../../05-fuentes/index.md#monnet2022)).

## VExUS

| Situación | Problema | Tipo de error | Fuente |
|---|---|---|---|
| **Fibrilación auricular** | Falta la onda A y la onda S disminuye (S < D) **sin aumento de la PAD** | Falso positivo (suprahepáticas) | [Assavapokee, 2024](../../05-fuentes/index.md#assavapokee2024) |
| Otras alteraciones del ritmo (PR largo) | Errores de interpretación sin ECG | Mala clasificación | [Assavapokee, 2024](../../05-fuentes/index.md#assavapokee2024) |
| **Cirrosis e infiltración grasa hepática** | Onda suprahepática aplanada, con pérdida de la fasicidad cardiaca | Falso negativo (suprahepáticas) | [Assavapokee, 2024](../../05-fuentes/index.md#assavapokee2024) |
| **Cirrosis e hipertensión portal** | Flujo portal continuo de baja velocidad, a veces pulsátil sin PAD elevada. En otros pacientes, la rigidez hepática atenúa la transmisión y la FPP es normal pese a una PAD alta | Falsos positivos y negativos (porta) | [Assavapokee, 2024](../../05-fuentes/index.md#assavapokee2024) |
| **Personas delgadas y deportistas** | Mayor pulsatilidad portal sin aumento de la PAD | Falso positivo (porta) | [Assavapokee, 2024](../../05-fuentes/index.md#assavapokee2024) |
| **Variación respiratoria de la porta** | Se confunde con la pulsatilidad cardiaca | Falso positivo; se evita con ECG | [Assavapokee, 2024](../../05-fuentes/index.md#assavapokee2024) |
| **Insuficiencia tricuspídea estructural grave** | Inversión persistente de la onda S que puede no mejorar al retirar volumen. Indica congestión, pero no necesariamente sobrecarga de volumen | «Falso positivo» respecto a la sobrecarga de volumen | [Assavapokee, 2024](../../05-fuentes/index.md#assavapokee2024) |
| **Disfunción crónica del VD o hipertensión pulmonar** | Una PVC crónicamente elevada produce congestión por **sobrecarga de presión**. El VExUS no distingue la sobrecarga de volumen de la de presión | Riesgo de interpretar «congestión» como «demasiado volumen» | [Assavapokee, 2024](../../05-fuentes/index.md#assavapokee2024); [Koratala, 2022](../../05-fuentes/index.md#koratala2022) |
| **Enfermedad renal crónica y trasplante renal** | El Doppler intrarrenal no se ha estudiado en estas poblaciones | Validez desconocida | [Assavapokee, 2024](../../05-fuentes/index.md#assavapokee2024) |
| **Ventana y colaboración** | El Doppler intrarrenal es el más difícil de obtener, sobre todo si el paciente no puede mantener la apnea | Exploración incompleta | [Assavapokee, 2024](../../05-fuentes/index.md#assavapokee2024) |
| **VCI < 2 cm con presión elevada** | Por hipertensión intraabdominal o en poblaciones con VCI más pequeña, se clasificaría como grado 0 | Falso negativo | [Assavapokee, 2024](../../05-fuentes/index.md#assavapokee2024) |

### Limitaciones de la evidencia del VExUS

- **Población de derivación:** 145 pacientes de **cirugía cardiaca** de un solo centro, en análisis *post hoc*. Allí el grado 3 tuvo una especificidad del 96 %, pero una **sensibilidad solo del 27 %** ([Beaubien-Souligny, 2020](../../05-fuentes/index.md#beaubien2020)).
- **UCI general:** baja prevalencia de congestión (grado 2 en el 16 % y grado 3 en el 6 %) y **sin asociación** con la LRA ni con la mortalidad ([Andrei, 2023](../../05-fuentes/index.md#andrei2023)).
- **Metaanálisis:**
    - Un VExUS ≥ 2 se asoció a la LRA en críticos (OR 2,63), pero **con una heterogeneidad alta** (I² 74 %) y sin asociación con la mortalidad ([Melo, 2025](../../05-fuentes/index.md#melo2025)).
    - En críticos no cardiacos, **ni la LRA ni la mortalidad** se asociaron a un VExUS ≥ 2, con certeza muy baja o baja ([Klompmaker, 2026](../../05-fuentes/index.md#klompmaker2026b)).
- **Sin ECA:** no se ha demostrado que actuar según el VExUS mejore los resultados. ANDROMEDA-VEXUS está en curso ([Prager, 2023](../../05-fuentes/index.md#prager2023)).
- **Reproducibilidad:** es sustancial entre médicos entrenados (κ 0,71), y mejor con ECG ([Longino, 2024b](../../05-fuentes/index.md#longino2024b)). Se desconoce la reproducibilidad con operadores poco experimentados.

!!! warning "Error frecuente"
    Tratar el grado de VExUS como un objetivo terapéutico («bajar a grado 0 con diuréticos») en un paciente con hipertensión pulmonar crónica o insuficiencia tricuspídea estructural. Allí la congestión puede ser crónica y poco modificable, y la retirada agresiva de volumen puede reducir el gasto ([Assavapokee, 2024](../../05-fuentes/index.md#assavapokee2024)). El VExUS se interpreta **en serie y en su contexto**, no como un número aislado.

## FoCUS en manos no expertas

### Función del VI «a ojo»

- La concordancia con el experto es sustancial (κ 0,68; S 89 %, E 85 %), pero los estudios son **pequeños, monocéntricos, de baja calidad y muy heterogéneos** ([Albaroudi, 2022](../../05-fuentes/index.md#albaroudi2022)).
- La FoCUS distingue una función normal, reducida o muy reducida. **No permite cuantificar** la FEVI con precisión ni valorar las válvulas ([Via, 2014](../../05-fuentes/index.md#via2014)).
- Un VI hiperdinámico **no diferencia** la hipovolemia de la sepsis precoz, porque ambas lo producen ([Mok, 2016](../../05-fuentes/index.md#mok2016)).

### Ventrículo derecho

- **Dilatación mal medida:** una visualización incompleta o un apical acortado (*foreshortening*) llevan a errores ([Blanco, 2016](../../05-fuentes/index.md#blanco2016)).
- **Dilatación crónica frente a aguda:** la sobrecarga crónica de volumen (insuficiencia tricuspídea o pulmonar) y la de presión (hipertensión pulmonar crónica) dilatan el VD sin relación con un TEP. Una pared libre > 5 mm sugiere cronicidad. El **infarto del VD** también lo dilata ([Blanco, 2016](../../05-fuentes/index.md#blanco2016)).
- **Rendimiento para el TEP:** la «sobrecarga del VD» tiene una sensibilidad del **53 %**, así que una ecocardioscopia normal **no descarta el TEP** ([Fields, 2017](../../05-fuentes/index.md#fields2017)).
- La relación VD/VI **no es válida si el VI está dilatado** ([Zaidi, 2020](../../05-fuentes/index.md#zaidi2020)).
- **TAPSE:** depende del ángulo y solo refleja la función longitudinal basal. Suele estar reducido tras la cirugía cardiotorácica ([Zaidi, 2020](../../05-fuentes/index.md#zaidi2020)).

### Derrame pericárdico

- Hay que diferenciarlo del **derrame pleural** (por detrás de la aorta descendente en el paraesternal largo), de la **ascitis** y de la **grasa epicárdica** ([Blanco, 2016](../../05-fuentes/index.md#blanco2016); [Seif, 2012](../../05-fuentes/index.md#seif2012)).
- El taponamiento es un **diagnóstico clínico-ecográfico**: un derrame sin colapso de cavidades puede no ser la causa del shock ([Alerhand, 2022](../../05-fuentes/index.md#alerhand2022)).

## Dependencia del operador y concordancia

| Medida | Concordancia o precisión | Fuente |
|---|---|---|
| FEVI visual (urgenciólogo frente a experto) | κ 0,68 (normal o anormal); κ ponderada 0,70 | [Albaroudi, 2022](../../05-fuentes/index.md#albaroudi2022) |
| Diámetros de la VCI (tres vistas) | Mejor concordancia con la vista longitudinal por la línea axilar media anterior (κ 0,69) | [Saul, 2012](../../05-fuentes/index.md#saul2012) |
| Diámetro de la VCI en modo B, eje largo | CCI 0,86. Los índices de colapso con modo M tuvieron CCI **bajos**, con dificultad para obtener la misma vista entre operadores | [Finnerty, 2017](../../05-fuentes/index.md#finnerty2017) |
| VTI (exploraciones sucesivas) | Cambio mínimo significativo del 11 % (mismo operador) y del 14 % (dos operadores) | [Jozwiak, 2019](../../05-fuentes/index.md#jozwiak2019) |
| VExUS (grado global) | κ 0,71; CCI 0,83. Mejor con ECG | [Longino, 2024b](../../05-fuentes/index.md#longino2024b) |

!!! info "Implicación práctica"
    Las medidas seriadas deberían hacerse, si es posible, **por el mismo operador y con la misma técnica documentada**: vista, punto de medida y modo. La formación y la acreditación se tratan en [08 · Formación](08-formacion.md).

## Errores cognitivos

Los errores de razonamiento con la ecografía son un tema de **opinión de expertos**: no se han localizado estudios que los cuantifiquen específicamente en el shock. Los más citados en la docencia son estos:

| Error | Ejemplo en el shock | Cómo evitarlo |
|---|---|---|
| **Anclaje** | Fijar el diagnóstico de «shock séptico» y no ver el derrame pericárdico o el VD dilatado | Seguir **un protocolo completo** (bomba, depósito, tuberías) aunque el primer hallazgo «encaje» |
| **«Un solo hallazgo»** | Decidir los fluidos solo por la VCI | La guía recomienda **no guiar la reanimación por una sola variable hemodinámica** ([Cecconi, 2014](../../05-fuentes/index.md#cecconi2014)) |
| **Cierre prematuro** | Encontrar un derrame pequeño y atribuirle el shock | Buscar signos de **fisiología** (colapso del VD o la AD, VCI pletórica) y otras causas ([Alerhand, 2022](../../05-fuentes/index.md#alerhand2022)) |
| **Satisfacción de búsqueda** | Tras confirmar una hipovolemia (VI hiperdinámico, VCI colapsada), no buscar su causa (hemoperitoneo, aneurisma roto) | Completar el «depósito con fugas» y las «tuberías» ([Seif, 2012](../../05-fuentes/index.md#seif2012)) |
| **Foto fija** | Una sola exploración al ingreso | **Reevaluar** tras cada intervención. Se recomienda la evaluación seriada del estado hemodinámico (nivel 1, calidad baja) ([Cecconi, 2014](../../05-fuentes/index.md#cecconi2014)) |
| **Confundir respuesta con necesidad** | «Responde a la EPP, luego le doy fluidos» | Dar fluidos solo si hay shock, responde a la precarga **y** el riesgo de sobrecarga es limitado ([Monnet, 2015](../../05-fuentes/index.md#monnet2015)) |
| **Sesgo de hallazgo incidental** | Un protocolo «talla única» genera hallazgos sin relación con el cuadro | Enfoque jerárquico por indicación clínica ([Milne, 2016](../../05-fuentes/index.md#milne2016)) |

La columna de ejemplos y de prevención es una elaboración docente. Las referencias apoyan el principio en que se basa cada fila.

## Shock mixto y hallazgos que se solapan

- **El shock puede deberse a varios mecanismos a la vez**, y un tipo puede evolucionar a otro ([Cecconi, 2014](../../05-fuentes/index.md#cecconi2014)). Ejemplos:
    - La **sepsis** combina vasodilatación, hipovolemia relativa y, a menudo, **disfunción miocárdica**, que aplana la curva de Frank-Starling ([Persichini, 2022](../../05-fuentes/index.md#persichini2022)). En la tabla SIMPLE, el shock séptico pasa de un VI hiperdinámico con VCI colapsada en fases precoces a un **VI hipocinético con VCI distendida** en fases tardías ([Mok, 2016](../../05-fuentes/index.md#mok2016)).
    - El **shock cardiogénico o hemorrágico** puede complicarse con una sepsis ([Cecconi, 2014](../../05-fuentes/index.md#cecconi2014)).
- **Hallazgos compartidos:**
    - Una **VCI pletórica** aparece en el shock cardiogénico, en el TEP y en el taponamiento, y también en la insuficiencia tricuspídea crónica ([Mok, 2016](../../05-fuentes/index.md#mok2016); [Blanco, 2016](../../05-fuentes/index.md#blanco2016)).
    - Un **VI hiperdinámico** aparece en la hipovolemia, en la sepsis precoz y en el TEP ([Mok, 2016](../../05-fuentes/index.md#mok2016)).
- **Pacientes con patología de base:** una miocardiopatía, una hipertensión pulmonar o una EPOC previas cambian el punto de partida. Un **perfil B pulmonar previo**, por ejemplo, invalida el FALLS ([Lichtenstein, 2013](../../05-fuentes/index.md#lichtenstein2013)).

!!! tip "Perla clínica"
    Ante un hallazgo que no encaja, conviene preguntarse **qué es agudo y qué es crónico**: pared del VD > 5 mm, aurículas dilatadas, historia previa ([Blanco, 2016](../../05-fuentes/index.md#blanco2016)). Si hay ecocardiogramas previos, compararlos. Para el hígado, compararlo con estudios de imagen anteriores también ayuda ([Assavapokee, 2024](../../05-fuentes/index.md#assavapokee2024)).

## Límites del RUSH y de los protocolos multiórgano

1. **Origen en la opinión de expertos.** El RUSH y el ACES se desarrollaron por consenso de usuarios expertos, **no a partir de datos prospectivos** ([Milne, 2016](../../05-fuentes/index.md#milne2016)).
2. **Sin beneficio demostrado en la supervivencia.** En el único ECA multicéntrico en urgencias (SHoC-ED, 273 pacientes), añadir un protocolo POCUS no cambió la supervivencia (104/136 frente a 102/134), ni el uso de TC, inotrópicos o fluidos, ni las estancias ([Atkinson, 2018](../../05-fuentes/index.md#atkinson2018)). El análisis de este y de otros ensayos está en [04 · Impacto clínico](04-impacto.md).
3. **Mayor precisión para confirmar que para descartar.** La sensibilidad es menor en el shock **distributivo**, del 78–79 % ([Yoshida, 2023](../../05-fuentes/index.md#yoshida2023); [Basmaji, 2025](../../05-fuentes/index.md#basmaji2025)). Véase [03 · Precisión](03-precision.md).
4. **«Talla única».** Los protocolos completos generan hallazgos incidentales. El SHoC propone un enfoque **jerárquico** con vistas nucleares, complementarias y adicionales ([Milne, 2016](../../05-fuentes/index.md#milne2016); [Atkinson, 2017](../../05-fuentes/index.md#atkinson2017)).
5. **Clasifican, pero no gestionan la reanimación.** El RUSH dice «qué tipo de shock es», pero su valoración del «depósito» se basa en la **VCI**, con todas sus limitaciones para predecir la respuesta ([Seif, 2012](../../05-fuentes/index.md#seif2012); [Orso, 2020](../../05-fuentes/index.md#orso2020)). La decisión de dar fluidos exige **medidas dinámicas** ([Monnet, 2025](../../05-fuentes/index.md#monnet2025)).
6. **Tiempo y recursos.** La exploración completa puede retrasar otras medidas. El propio RUSH propone hacerla abreviada y a la carta ([Seif, 2012](../../05-fuentes/index.md#seif2012)).
7. **No sustituye a las pruebas de confirmación** (TC, ecocardiografía reglada, analítica) cuando son accesibles y el paciente lo permite. La ecografía es sobre todo una prueba para **confirmar**, más que para descartar, en el TEP ([Fields, 2017](../../05-fuentes/index.md#fields2017)).

## Tabla resumen: trampas y cómo evitarlas

| Herramienta | Trampa principal | Cómo evitarla |
|---|---|---|
| VCI | Esfuerzo inspiratorio, hipertensión intraabdominal, VD o insuficiencia tricuspídea, traslación, punto de medida | Estandarizar la maniobra; comprobar en 2D y en eje corto; no usarla sola |
| VTI | Ángulo, arritmias, cambio mínimo significativo del 11 % | Mismo operador y punto; promediar 3–5 latidos; desconfiar de cambios < 10–15 % |
| EPP | Hipertensión intraabdominal, dolor, empezar en supino, medir la presión | Seguir las cinco reglas; medir el flujo en tiempo real |
| VExUS | FA, cirrosis, VD o insuficiencia tricuspídea crónicos, ERC, ventana | ECG; contexto clínico; comparar con estudios previos; seriar |
| FoCUS | VD crónico frente a agudo, derrame frente a grasa o pleura, FEVI «a ojo» | Varias ventanas; signos de cronicidad; preguntas binarias |
| Protocolos (RUSH) | Anclaje, hallazgo único, falsa seguridad ante una exploración normal | Protocolo completo pero dirigido; reevaluar; integrar en la clínica |

## Puntos clave

- La **VCI** es poco fiable para predecir la respuesta a fluidos. Falla con los esfuerzos respiratorios, la hipertensión intraabdominal, la disfunción del VD o la insuficiencia tricuspídea, los errores técnicos (traslación, efecto cilindro, punto de medida) y en los deportistas. **Nunca debe usarse sola** ([Orso, 2020](../../05-fuentes/index.md#orso2020); [Blanco, 2016](../../05-fuentes/index.md#blanco2016); [Cardozo Júnior, 2023](../../05-fuentes/index.md#cardozo2023)).
- La **VTI** depende del ángulo, de la ventana y del ritmo. Su **cambio mínimo significativo es del 11–14 %**, lo que cuestiona los umbrales pequeños, como el 5 % del mini-bolo ([Jozwiak, 2019](../../05-fuentes/index.md#jozwiak2019)).
- La **EPP** da **falsos negativos con hipertensión intraabdominal** y falsos positivos con dolor o estimulación adrenérgica. Está contraindicada en la hipertensión intracraneal ([Beurton, 2019](../../05-fuentes/index.md#beurton2019); [Monnet, 2022](../../05-fuentes/index.md#monnet2022)).
- El **VExUS** se altera sin sobrecarga de volumen en la FA, la cirrosis, las personas delgadas y la insuficiencia tricuspídea o disfunción del VD crónicas. No distingue la sobrecarga de volumen de la de presión, y su valor pronóstico fuera de la cirugía cardiaca es incierto ([Assavapokee, 2024](../../05-fuentes/index.md#assavapokee2024); [Klompmaker, 2026](../../05-fuentes/index.md#klompmaker2026b)).
- La **FoCUS no experta** valora bien la función del VI de forma cualitativa (κ 0,68). Tiene más problemas con el VD, porque hay que distinguir lo agudo de lo crónico, y **una exploración normal no descarta el TEP** (sensibilidad del 53 %) ([Albaroudi, 2022](../../05-fuentes/index.md#albaroudi2022); [Fields, 2017](../../05-fuentes/index.md#fields2017)).
- Los **errores cognitivos** (anclaje, hallazgo único, cierre prematuro) y el **shock mixto** son habituales. Se combaten con un protocolo completo, varias variables y **reevaluación seriada** ([Cecconi, 2014](../../05-fuentes/index.md#cecconi2014)).
- El **RUSH** es un marco docente de expertos que no ha demostrado beneficio en la supervivencia. Clasifica el shock, pero **no decide los fluidos**: para eso hacen falta medidas dinámicas ([Milne, 2016](../../05-fuentes/index.md#milne2016); [Atkinson, 2018](../../05-fuentes/index.md#atkinson2018)).

## Lagunas y preguntas abiertas

- **Errores cognitivos con la ecografía en el shock:** no se han localizado estudios que los cuantifiquen. Todo lo recogido es opinión de expertos.
- **VCI pequeña fisiológica en jóvenes o personas delgadas** como causa de falsos positivos: `[POR VERIFICAR]`, sin fuente primaria localizada.
- **EPP en amputados o con fracturas de pelvis o de las extremidades inferiores:** no hay estudios específicos `[POR VERIFICAR]`.
- **VExUS en la ERC, el trasplante renal, la FA y la cirrosis:** falta validación ([Assavapokee, 2024](../../05-fuentes/index.md#assavapokee2024)).
- **Reproducibilidad del VExUS y de la VTI con operadores noveles:** se desconoce. Los estudios disponibles son de operadores entrenados ([Longino, 2024b](../../05-fuentes/index.md#longino2024b); [Jozwiak, 2019](../../05-fuentes/index.md#jozwiak2019)).
- **Beneficio clínico de los protocolos:** el único ECA es negativo y antiguo (2012–2016), con predominio de sepsis ([Atkinson, 2018](../../05-fuentes/index.md#atkinson2018)).

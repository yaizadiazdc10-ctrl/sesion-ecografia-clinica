# 09 · Novedades y controversias

La ecografía pulmonar en la disnea y la IC se mueve rápido. Hay algoritmos de inteligencia artificial (IA) que cuentan líneas B o guían al operador novel, sondas de bolsillo conectadas al móvil y pacientes que se hacen la ecografía en casa. En paralelo, persisten debates abiertos: puntuación cuantitativa o valoración cualitativa, si la LUS puede sustituir a la radiografía, y si los metaanálisis recientes sobrestiman el beneficio.

Esta página resume lo nuevo (2021–2026), qué evidencia hay detrás de cada novedad y qué ensayos pueden cambiar la práctica en los próximos años. Para la evidencia de impacto consolidada, véase [04-impacto](04-impacto.md). Para las limitaciones técnicas, [07-limitaciones](07-limitaciones.md).

!!! abstract "En pocas líneas"
    - La **IA ya permite que personal no experto adquiera imágenes pulmonares de calidad diagnóstica**, al menos en un estudio de validación ([Baloescu, 2025](../../05-fuentes/index.md#baloescu2025)).
    - La **cuantificación automática de líneas B es heterogénea**: excelente en algunos algoritmos de investigación y pobre en un software comercial evaluado ([Goldsmith, 2023](../../05-fuentes/index.md#goldsmith2023); [Labaf, 2025](../../05-fuentes/index.md#labaf2025)).
    - La **autoexploración domiciliaria** es factible, pero todavía no ha demostrado beneficio clínico.
    - Los **metaanálisis de 2026** coinciden en menos visitas urgentes por IC, discrepan en la hospitalización y **ninguno muestra efecto sobre la mortalidad**.

---

## 1. Inteligencia artificial en la ecografía pulmonar

### 1.1. IA para adquirir la imagen: guiado de no expertos

El hito reciente es un estudio multicéntrico de validación diagnóstica con 176 participantes con disnea. **Personal sanitario no médico** (auxiliares, fisioterapeutas respiratorios y enfermeras), formado en un software de guiado por IA, adquirió exploraciones pulmonares de 8 zonas. Un panel ciego de 5 expertos consideró de **calidad diagnóstica el 98,3 %** (IC 95 % 95,1–99,4 %). No hubo diferencias significativas con las exploraciones de expertos sin IA: diferencia de 1,7 % (IC 95 % −1,6 a 5,0 %) ([Baloescu, 2025](../../05-fuentes/index.md#baloescu2025)).

!!! note "Qué demuestra y qué no"
    Este estudio demuestra **calidad de imagen**, no precisión diagnóstica en manos del no experto ni impacto clínico. La interpretación final la hicieron expertos en remoto ([Baloescu, 2025](../../05-fuentes/index.md#baloescu2025)).

### 1.2. IA para interpretar: cuantificación automática de líneas B

| Estudio (año) | Datos | Comparación | Resultado | Cita |
|---|---|---|---|---|
| Russell 2021 | 51 principiantes, 29 pacientes con ICA, 611 zonas | IA sobre imágenes de principiantes frente a expertos | Concordancia **moderada o regular**: CCI de 0,56, frente a 0,82 entre expertos | [Russell, 2021](../../05-fuentes/index.md#russell2021) |
| Goldsmith 2023 (análisis secundario de BLUSHED-AHF) | 3858 clips, 130 pacientes | Puntuación de congestión por IA frente a 2 expertos | Correlación **alta**: r de 0,894 y 0,882. Los expertos concordaron más con la IA que con el operador original | [Goldsmith, 2023](../../05-fuentes/index.md#goldsmith2023) |
| Pare 2024 | 49 952 fotogramas de entrenamiento. Validación en 476 clips de 60 pacientes | Red neuronal convolucional (aprendizaje por transferencia) frente a experto | AUC de 0,967 para detectar patología. Kappa ponderado de 0,839 en la escala 0–4 | [Pare, 2024](../../05-fuentes/index.md#pare2024) |
| Baloescu 2024 | 110 pacientes, 3379 clips | Puntuación de líneas B por aprendizaje profundo frente a evolución clínica | Se asocia a la puntuación clínica de congestión (coeficiente de 0,7), pero no al índice de Rothman | [Baloescu, 2024](../../05-fuentes/index.md#baloescu2024) |
| **Labaf 2025** | 55 pacientes, 672 zonas (protocolo de 12 zonas) | **Software de IA integrado en un ecógrafo comercial** frente a 2 expertos | Concordancia **pobre** (CCI de 0,28 para la suma total). La IA **sobrecontó** las líneas B (23,5 frente a 2,8 por paciente). Entre expertos, CCI de 0,92 | [Labaf, 2025](../../05-fuentes/index.md#labaf2025) |
| Coiro 2024 | Cohorte de urgencias (n = 117) + validación externa | Árbol de decisión de aprendizaje automático sobre LUS de 8 zonas para el diagnóstico de ICA | AUC de 0,865 en desarrollo y de 0,906 en validación. Muy alto riesgo con ≥ 14 líneas B bilaterales | [Coiro, 2024](../../05-fuentes/index.md#coiro2024) |

!!! warning "Error frecuente: confiar ciegamente en el contador automático del ecógrafo"
    Los algoritmos de investigación (Goldsmith, Pare) muestran buena concordancia con los expertos. Pero la única evaluación independiente publicada de un software comercial encontró una **sobreestimación de casi diez veces** en el número de líneas B ([Labaf, 2025](../../05-fuentes/index.md#labaf2025)). Antes de usar un contador automático para ajustar diuréticos, compruébalo con tu propio recuento. La validación varía de un fabricante a otro y de una versión a otra.

### 1.3. IA y simplificación del protocolo

En 205 pacientes con IC conocida o sospechada (5728 vídeos), un algoritmo de aprendizaje profundo comparó un protocolo de **2 zonas anterosuperiores** con el de 8 zonas. No encontró diferencias en la gravedad media: diferencia de 0,03 en una escala de 0 a 4 ([Baloescu, 2023](../../05-fuentes/index.md#baloescu2023)). Es un dato interesante para simplificar el seguimiento, pero se trata de un estudio observacional. El protocolo recomendado por la EACVI sigue siendo el de 8 zonas ([Gargani, 2023](../../05-fuentes/index.md#gargani2023)).

---

## 2. Dispositivos de bolsillo, tele-ecografía y telemonitorización

### 2.1. Ecógrafos de bolsillo

- **Rendimiento frente a equipos convencionales**. En medicina interna, un ecógrafo de bolsillo concordó con un equipo convencional en el **79 %** para las líneas B, el **89 %** para el derrame y el **82 %** para las consolidaciones. La exploración fue algo más rápida: 8 ± 1,5 frente a 10 ± 2,5 min ([Lo Cricchio, 2024](../../05-fuentes/index.md#locricchio2024)).
- **Ya se usaban en estudios clave**. El estudio pronóstico ambulatorio de Platz se hizo con ecógrafo de bolsillo, con una exploración mediana de unos 2 minutos ([Platz, 2016](../../05-fuentes/index.md#platz2016)). También el ensayo LUS-HF ([Rivas-Lasarte, 2019](../../05-fuentes/index.md#rivaslasarte2019)).
- **Contextos con pocos recursos**. En Tanzania rural, clínicos de primaria formados en unas 8 horas concordaron con ecografistas expertos en el **93 %** de los hallazgos. La concordancia con los médicos sénior fue sustancial en el diagnóstico de IC (85 %; κ = 0,69), pero **ligera en la neumonía** (κ = 0,002–0,06) ([Katende, 2024](../../05-fuentes/index.md#katende2024)).

### 2.2. Enfermería y otros profesionales

- **Enfermeras de IC**. Hicieron una valoración de pulmón y VCI de 9 zonas antes del alta a 240 pacientes. Los congestionados tuvieron más reingresos o muertes a 90 días (37 % frente a 14 %) ([Zisis, 2022](../../05-fuentes/index.md#zisis2022)).
- **Intervención liderada por enfermería**. Aplicada como intervención (DMP-Plus), no mejoró los resultados ([Zisis, 2024](../../05-fuentes/index.md#zisis2024)).
- **Hospitalización a domicilio**. En Calgary, el protocolo **ACCUMEN-POCUS** tiene paramédicos comunitarios que adquieren ecografías de pulmón y VCI en el domicilio, y médicos que las interpretan en remoto en tiempo real. Es un ECA de factibilidad con 20 pacientes, con el análisis todavía en curso ([Grinman, 2025](../../05-fuentes/index.md#grinman2025)).

### 2.3. Autoexploración domiciliaria por el paciente

| Estudio (año) | n | Modelo | Resultado | Cita |
|---|---|---|---|---|
| Patient-PLUS, Chiem 2021 | 44 pacientes con IC (el 70 % con estudios secundarios o inferiores) | Formación de 15 min. LUS de 4 zonas con sonda portátil. Revisión remota | El **85 %** de las zonas fueron interpretables. Acuerdo entre expertos del 87 % (κ = 0,49). El 98 % se veía capaz de hacerlo en casa | [Chiem, 2021](../../05-fuentes/index.md#chiem2021) |
| Pratzer 2023 | 8 pacientes estables, 89 sesiones | Autoexploración de 6 zonas en casa con **tele-guiado** en directo por un clínico | El 84–88 % de los clips fueron interpretables. Unos 5 minutos por sesión. Sin falsos positivos | [Pratzer, 2023](../../05-fuentes/index.md#pratzer2023) |
| HOUSE-HF, Prenner 2025 | 15 pacientes tras un ingreso por ICA | Formación de 20 min. 6 zonas, 3 veces por semana durante 3 semanas. Subida a la nube | Se obtuvo el 99,5 % de las imágenes y el **80,8 % fueron interpretables**. La zona lateral inferior izquierda fue la más difícil (69,5 %) | [Prenner, 2025](../../05-fuentes/index.md#prenner2025) |

!!! info "Estado de la cuestión"
    La autoexploración es **factible en estudios piloto pequeños**. No hay todavía ningún ECA que demuestre que detecta antes la descompensación o que reduce los ingresos ([Chiem, 2021](../../05-fuentes/index.md#chiem2021); [Pratzer, 2023](../../05-fuentes/index.md#pratzer2023); [Prenner, 2025](../../05-fuentes/index.md#prenner2025)). Las zonas laterales y posterolaterales, las más sensibles para la congestión, son las que peor se autoexploran ([Prenner, 2025](../../05-fuentes/index.md#prenner2025)).

---

## 3. Lo aprendido con la COVID-19

La pandemia disparó el uso de la LUS: portabilidad, menos traslados de pacientes contagiosos y posibilidad de repetirla sin radiación. Lecciones con evidencia:

- **Sensible, pero poco específica para el diagnóstico etiológico**. En la revisión Cochrane, la LUS tuvo una sensibilidad agrupada del **88,9 %** y una especificidad del **72,2 %** (15 estudios, 2410 participantes). Su sensibilidad fue similar a la de la TC y mayor que la de la Rx, con especificidades comparables entre las tres ([Ebrahimzadeh, 2022](../../05-fuentes/index.md#ebrahimzadeh2022)).
- **Resultados similares en urgencias**: sensibilidad del 87,2 % y especificidad del 69,5 %, con estudios de baja calidad y hechos en periodos de alta prevalencia ([Matthies, 2023](../../05-fuentes/index.md#matthies2023)).
- **Puntuaciones cuantitativas con valor pronóstico**. El LUS score fue más alto en los fallecidos (diferencia media ponderada de 8,21) y aumentó con la gravedad ([Song, 2021](../../05-fuentes/index.md#song2021)).

!!! tip "Perla clínica: el patrón B no es sinónimo de IC"
    La COVID recordó que un **patrón B bilateral también aparece en la neumonía viral y en el SDRA**. La especificidad de la LUS para una etiología concreta es moderada ([Ebrahimzadeh, 2022](../../05-fuentes/index.md#ebrahimzadeh2022)). Para distinguir el edema cardiogénico hay que **integrar**:

    - la morfología de la línea pleural y la distribución de las líneas B (homogénea o parcheada), cuyos criterios se detallan en [precisión](03-precision.md);
    - el corazón y la VCI;
    - la clínica.

    Integrar LUS y ecografía cardiaca eleva la especificidad para la ICA al 96 % ([Popat, 2026](../../05-fuentes/index.md#popat2026)). Más en [precisión](03-precision.md).

---

## 4. Controversia: LUS score cuantitativo frente a valoración cualitativa

| Postura | Fundamento | Cita |
|---|---|---|
| **A favor de contar** (cuantitativo) | El protocolo de 8 zonas con recuento de líneas B es el más usado en la IC. La congestión residual al alta cuantificada tiene valor pronóstico | [Gargani, 2023](../../05-fuentes/index.md#gargani2023); [Rastogi, 2024](../../05-fuentes/index.md#rastogi2024) |
| **En contra en el nivel básico** (ESICM) | La ESICM recomienda **no usar puntuaciones cuantitativas (LUS score) como ecografía básica** (recomendación fuerte en contra). Prioriza reconocer patrones: patrón B, consolidación | [Robba, 2021](../../05-fuentes/index.md#robba2021) |
| Consenso internacional | Adaptar la técnica a la situación clínica y explorar la mayor superficie posible | [Demi, 2023](../../05-fuentes/index.md#demi2023) |
| Simplificación | 4 zonas con valor pronóstico, o 2 zonas equivalentes a 8 con IA | [Platz, 2019](../../05-fuentes/index.md#platz2019); [Baloescu, 2023](../../05-fuentes/index.md#baloescu2023) |

!!! note "Cómo conciliarlo"
    Las dos posturas responden a preguntas y ámbitos distintos:

    - La ESICM habla de **competencias básicas del intensivista**, donde lo esencial es reconocer patrones.
    - La EACVI habla del **seguimiento de la IC**, donde el cambio en el número de líneas B es precisamente el objetivo terapéutico ([Robba, 2021](../../05-fuentes/index.md#robba2021); [Gargani, 2023](../../05-fuentes/index.md#gargani2023)).

    En la charla puede presentarse así: **patrón para diagnosticar; número para seguir la evolución**. *Esta síntesis es opinión del equipo, no una recomendación formal.*

La otra cara del recuento es la **heterogeneidad de los umbrales**, que dificulta comparar ensayos. Los ensayos usan ≥ 3, ≥ 5, ≥ 10, > 15 o ≥ 30 líneas B según el número de zonas ([Platz, 2017](../../05-fuentes/index.md#platz2017); [Chotalia, 2026](../../05-fuentes/index.md#chotalia2026)).

---

## 5. Integración con VExUS: la congestión multiorgánica

El concepto emergente es el **fenotipado de la congestión**:

- **Pulmonar**, por LUS, que refleja sobre todo la presión de enclavamiento.
- **Venosa sistémica**, por VCI y VExUS, que refleja sobre todo la presión de aurícula derecha ([Jimenez, 2026](../../05-fuentes/index.md#jimenez2026)).

Ambos componentes pueden disociarse. En DRY-OFF, la congestión intravascular mejoró más con el diurético en la FEVI reducida que en la preservada ([Cogliati, 2022](../../05-fuentes/index.md#cogliati2022)).

La evidencia del VExUS en la ICA es **pronóstica**: VExUS 3 al ingreso o al alta se asocia a más mortalidad y reingreso ([Anastasiou, 2024](../../05-fuentes/index.md#anastasiou2024); [Anastasiou, 2026](../../05-fuentes/index.md#anastasiou2026)). Su mejora dinámica se asocia a menos mortalidad ([Saadi, 2025](../../05-fuentes/index.md#saadi2025)). Falta demostrar que **guiar** el tratamiento con VExUS mejore los resultados: el único ECA, en síndrome cardiorrenal, fue negativo en su objetivo primario ([Islas-Rodríguez, 2024](../../05-fuentes/index.md#islasrodriguez2024)). El ensayo español **ABDOPOCUS-HF**, que combina presión intraabdominal, LUS, VCI y VExUS, está en reclutamiento ([Josa-Laorden, 2025](../../05-fuentes/index.md#josalaorden2025)). Detalle en [04-impacto, sección 4](04-impacto.md#4-estrategias-multiorganicas-de-descongestion).

---

## 6. Debate: ¿sustituye la LUS a la radiografía de tórax?

**A favor de la LUS**

- Detecta el edema cardiogénico **mejor que la radiografía**: sensibilidad del 88 % frente al 73 % en Maw, y del 91,8 % frente al 76,5 % en Chiu, con especificidad igual o mayor ([Maw, 2019](../../05-fuentes/index.md#maw2019); [Chiu, 2022](../../05-fuentes/index.md#chiu2022)).
- En un ECA en urgencias, añadir LUS a la clínica fue más preciso que añadir Rx + NT-proBNP: AUC de 0,95 frente a 0,87 ([Pivetta, 2019](../../05-fuentes/index.md#pivetta2019)).
- Da el resultado en el momento. En un estudio clásico, la radiografía tardaba de media 1 h 35 min hasta el informe. En los casos discordantes, la TC dio la razón a la ecografía en el 63 % ([Zanobetti, 2011](../../05-fuentes/index.md#zanobetti2011)).
- Reduce las radiografías y las TC en la UCI (−26 % y −47 % en un estudio antes-después) ([Peris, 2010](../../05-fuentes/index.md#peris2010)).
- No irradia y puede repetirse para monitorizar.

**En contra de sustituirla**

- La precisión depende del operador. Con no expertos, el beneficio es pequeño (NNS de 16) ([Baker, 2020](../../05-fuentes/index.md#baker2020)).
- El POCUS integrado fue **menos preciso que el estudio estándar para EPOC/asma y TEP** ([Zanobetti, 2017](../../05-fuentes/index.md#zanobetti2017)).
- La LUS solo explora lo que llega a la superficie pleural, así que la radiografía sigue aportando información en otras preguntas. *Es un límite físico de la técnica, no un dato de estos ensayos*; se desarrolla con citas en [07-limitaciones](07-limitaciones.md).
- Sustituir el circuito diagnóstico estándar por un circuito guiado por POCUS **no acortó la estancia** ([Ovesen, 2026](../../05-fuentes/index.md#ovesen2026)).

!!! note "Postura de síntesis (opinión del equipo)"
    Con la evidencia actual, lo razonable es presentar la LUS como **la primera prueba de imagen a pie de cama para la pregunta «¿hay edema pulmonar o congestión?»**. En esa pregunta supera a la Rx. No es un sustituto universal de la radiografía en la disnea. La ACP la sitúa **como complemento** de la vía estándar cuando hay incertidumbre ([Qaseem, 2021](../../05-fuentes/index.md#qaseem2021)).

---

## 7. Críticas a los metaanálisis recientes

El metaanálisis de **Al-Sagban 2026** (9 ECA, 1095 pacientes) es el más citado: RR de 0,72 para hospitalización por IC o muerte ([Al-Sagban, 2026](../../05-fuentes/index.md#alsagban2026)). Puntos críticos:

1. **Carta publicada**. *J Crit Care* ha publicado un comentario de Kumar et al. ([Kumar, 2026](../../05-fuentes/index.md#kumar2026)). Sus argumentos concretos quedan `[POR VERIFICAR]`: PubMed no incluye resumen y el texto completo es de pago.
2. **Modelo estadístico**. Según su propio resumen, Al-Sagban usó un **modelo de efectos fijos** ([Al-Sagban, 2026](../../05-fuentes/index.md#alsagban2026)). Otros metaanálisis contemporáneos no reproducen el efecto sobre la hospitalización en todos los análisis:
    - Chotalia 2026, en IC crónica: RR de 0,76, no significativo ([Chotalia, 2026](../../05-fuentes/index.md#chotalia2026)).
    - Bagheri 2026, subgrupo de LUS sola con efectos aleatorios: RR de 0,75, no significativo ([Bagheri, 2026](../../05-fuentes/index.md#bagheri2026)).
    - *Esta observación es del equipo y no sustituye a la lectura de la carta.*
3. **Resultados dominados por las visitas urgentes**, un objetivo blando, en ensayos abiertos o con un solo ciego ([Rivas-Lasarte, 2019](../../05-fuentes/index.md#rivaslasarte2019); [Araiza-Garaygordobil, 2020](../../05-fuentes/index.md#araizagaraygordobil2020)).
4. **Mezcla de ámbitos** (ambulatorio, alta y urgencias) y de protocolos. Algunos ensayos «de tratamiento guiado» tienen un objetivo primario de imagen o de proceso: el cambio de dosis en Cruz 2024 o la congestión al alta en CAVAL US-AHF ([Cruz, 2024](../../05-fuentes/index.md#cruz2024); [Burgos, 2024](../../05-fuentes/index.md#burgos2024)).
5. **Estudios no aleatorizados presentados como ensayos** (LUDT-ADHF). Conviene comprobar que ningún metaanálisis los incluya como ECA ([Kashoob, 2025](../../05-fuentes/index.md#kashoob2025)). `[POR VERIFICAR]`: la lista exacta de ECA incluidos en Al-Sagban 2026 (no está en el resumen).

---

## 8. Ensayos y estudios en marcha

| Estudio | Registro | Diseño y n | Ámbito | Pregunta | Estado (consultado en sept. 2026) | Cita |
|---|---|---|---|---|---|---|
| **ICARUS** | NCT06465498 | ECA multicéntrico con enmascaramiento múltiple, n = 222 | ICA hospitalizada, Suiza | Descongestión guiada por LUS (8 puntos, diaria) frente a exploración física. Objetivo: días vivo y fuera del hospital a 40 días | Reclutando. Fin del objetivo primario previsto en 2027 | [Leidi, 2026](../../05-fuentes/index.md#leidi2026) |
| **ABDOPOCUS-HF** | NCT07008365 | ECA abierto y pragmático, n = 168 | ICA, 14 hospitales españoles | Presión intraabdominal + LUS + VCI + VExUS. Objetivo: escala ADVOR a las 72 h | Reclutando | [Josa-Laorden, 2025](../../05-fuentes/index.md#josalaorden2025) |
| **LUC REED** | NCT06807983 | ECA por clústeres con diseño *stepped-wedge*, n = 504 | Urgencias, mayores de 65 años con disnea grave, Francia | Estrategia guiada por LUS + ecografía cardiaca. Objetivo: **tratamiento inapropiado** en la primera hora | Aprobado en 2025 | [Balen, 2025](../../05-fuentes/index.md#balen2025) |
| **EMERALD-US** | NCT03691857 | Estudio diagnóstico, n = 225 | Urgencias, mayores de 50 años, 6 centros franceses | Rendimiento de un algoritmo de pulmón, corazón (4 cámaras) y venas | Protocolo publicado en 2025 | [Jaeger, 2025](../../05-fuentes/index.md#jaeger2025) |
| **ACCUMEN-POCUS** | NCT05423652 | ECA de factibilidad, n = 20 | Hospitalización a domicilio (EPOC, ICA, neumonía), Canadá | Ecografía de pulmón y VCI por paramédicos, interpretada en remoto | Reclutamiento cerrado. Análisis en curso | [Grinman, 2025](../../05-fuentes/index.md#grinman2025) |
| **EPICAP** | — | Cohorte prospectiva, n = 192 | **Atención primaria**, Barcelona. IC con FEVI ≥ 50 % | Valor pronóstico de la LUS (28 zonas, sonda de bolsillo) | Protocolo publicado en 2025 | [Leceaga-Gaztambide, 2025](../../05-fuentes/index.md#leceagagaztambide2025) |
| **IMP-OUTCOME** | NCT05035459 | Diseño prospectivo aleatorizado según el protocolo, n = 318 previstos | IC al alta con ≥ 3 líneas B, China | Manejo intensivo guiado por líneas B tras el alta | Estado **desconocido** en ClinicalTrials.gov. Sin resultados localizados | [Zhu, 2022](../../05-fuentes/index.md#zhu2022) |
| Volumen y momento del alta guiados por ecografía | NCT07046169 | ECA, n = 150 | IC hospitalizada, China | Objetivo: reingreso por IC o muerte cardiaca a 1 año | Activo, sin reclutar. Fin del objetivo primario previsto en julio de 2026 | [ClinicalTrials.gov NCT07046169](../../05-fuentes/index.md#nct07046169) |
| **FOCUS-ADHF** | NCT06726109 | Registro observacional, n = 600 | ICA, Bélgica e Italia | Resultados a largo plazo | Reclutando hasta 2030 | [ClinicalTrials.gov NCT06726109](../../05-fuentes/index.md#nct06726109) |

!!! info "Qué ensayos pueden cambiar la práctica"
    - **ICARUS** responderá a la pregunta que BLUSHED-AHF dejó abierta: ¿guiar la descongestión con LUS en el hospitalizado mejora los resultados clínicos ([Leidi, 2026](../../05-fuentes/index.md#leidi2026))?
    - **LUC REED** medirá directamente el resultado con más plausibilidad biológica en la disnea: el tratamiento inapropiado en el anciano ([Balen, 2025](../../05-fuentes/index.md#balen2025)), que se asocia a mortalidad ([Ray, 2006](../../05-fuentes/index.md#ray2006)).
    - **ABDOPOCUS-HF** es español y multiórgano, y encaja bien con el consenso SEMI/SEC/S.E.N. sobre la sobrecarga hidrosalina ([Llàcer, 2024](../../05-fuentes/index.md#llacer2024)).

---

## 9. Lagunas globales

- **Mortalidad**. Ningún ECA ni metaanálisis demuestra reducción de la mortalidad, ni en la disnea ([Szabó, 2023](../../05-fuentes/index.md#szabo2023)) ni en la IC ([Bagheri, 2026](../../05-fuentes/index.md#bagheri2026)).
- **Heterogeneidad** de protocolos, umbrales y algoritmos terapéuticos ([Chotalia, 2026](../../05-fuentes/index.md#chotalia2026)).
- **Sesgo de operador**:
    - Los ECA positivos se hicieron con operadores entrenados.
    - El efecto se diluye con experiencia variable ([Riishede, 2021](../../05-fuentes/index.md#riishede2021); [Baker, 2020](../../05-fuentes/index.md#baker2020)).
    - La IA comercial todavía no garantiza un recuento fiable ([Labaf, 2025](../../05-fuentes/index.md#labaf2025)).
- **Enmascaramiento**. Es imposible cegar al clínico, y los objetivos blandos predominan.
- **Implantación real**. Incluso con formación completa, solo el 20 % de las exploraciones las hicieron los hospitalistas de forma autónoma ([Maganti, 2025](../../05-fuentes/index.md#maganti2025)).
- **Atención primaria y domicilio**: evidencia limitada a factibilidad y cohortes en marcha.
- **Faltan estudios de coste-efectividad** formales.

## Puntos clave

- La **IA** permite a personal no experto adquirir imágenes pulmonares de calidad diagnóstica (98 %) ([Baloescu, 2025](../../05-fuentes/index.md#baloescu2025)). Los contadores automáticos de líneas B varían mucho: uno comercial sobrecontó casi diez veces ([Labaf, 2025](../../05-fuentes/index.md#labaf2025)).
- Los **ecógrafos de bolsillo** rinden de forma aceptable frente a los convencionales. La **autoexploración** del paciente con IC es factible (80–88 % de imágenes interpretables), pero **sin beneficio clínico demostrado** ([Lo Cricchio, 2024](../../05-fuentes/index.md#locricchio2024); [Prenner, 2025](../../05-fuentes/index.md#prenner2025)).
- La **COVID** enseñó que el patrón B es sensible pero poco específico de la causa: hay que integrarlo con la línea pleural, el corazón y la clínica ([Ebrahimzadeh, 2022](../../05-fuentes/index.md#ebrahimzadeh2022)).
- **Cuantitativo frente a cualitativo**: la ESICM desaconseja el LUS score en el nivel básico; la EACVI estandariza el recuento en 8 zonas para la IC. *Patrón para diagnosticar, número para seguir la evolución* ([Robba, 2021](../../05-fuentes/index.md#robba2021); [Gargani, 2023](../../05-fuentes/index.md#gargani2023)).
- La **LUS supera a la Rx** en la pregunta del edema, pero no la sustituye en toda disnea. Los circuitos POCUS sistemáticos no acortaron la estancia ([Maw, 2019](../../05-fuentes/index.md#maw2019); [Ovesen, 2026](../../05-fuentes/index.md#ovesen2026)).
- Los **metaanálisis de 2026** tienen resultados discordantes en la hospitalización y ninguno muestra efecto en la mortalidad. El de Al-Sagban usa efectos fijos y tiene una carta crítica publicada ([Al-Sagban, 2026](../../05-fuentes/index.md#alsagban2026); [Kumar, 2026](../../05-fuentes/index.md#kumar2026)).
- **ICARUS, ABDOPOCUS-HF y LUC REED** son los ensayos que pueden cambiar la práctica en 2027–2028.

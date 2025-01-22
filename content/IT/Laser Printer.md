---
tags:
  - hardware
---
Printing through electro-photographic imaging or LED arrays.
![[Laser Printer-20240725022239234.webp|313]]
Relies on photoconductive materials that conduct electricity when exposed to light.
Most laser printers are monochrome only.
These printers use a LOT of electricity.
Laser printers that print color can produce spot colors which are vibrant and high quality.
Color laser printers use [[CMYK]] as 4 separate toner cartridges
# Process
### Processing
1. PC creates [[Raster]] images
2. PC uses printer's [[Raster Image Processor]] driver to turn raster image into a series of commands to the laser.
3. Images are sent to the printer spooler, which handles print jobs
4. Printer spooler sends print job to printer
5. Commands are stored in RAM
   - Insufficient memory results in [[Memory Overflow]] errors.
	   - You can reduce image resolution or color depth to reduce filesize
	   - You can disable [[Resolution Enhancement Technology]]
   - Images that are too complex will result in complexity errors
### Charging
Primary Corona Wire applies a uniform 600V - 1000V negative charge to entire surface of Drum
   ![[Laser Printer-20240725042647779.webp|378]]
### Exposing
Laser used to create a remove negative charge on the drum correlating the places where image dots would be
### Developing
Particles with less negative charge (those hit by the laser) will attract toner particles, thereby creating a developed image.
![[Pasted image 20240725003006.png|397]]
### Transferring
Transfer Corona Wire gives the paper a positive charge, allowing the toner to transfer onto the paper.
### Fusing
1. Pressure roller applies pressure onto the paper
2. Heating roller melts toner onto paper, thereby permanently affixing it
3. Static discharge eliminator removes paper's positive charge
![[Laser Printer-20240725043149365.webp|418]]
### Cleaning
##### Drum Cleaning
Remove all residual toner by using a rubber cleaning blade along the surface of the drum.
![[Laser Printer-20240725043328216.webp|416]]
Allow the toner to fall into the cleaning mechanism where it may be reused
Erase lamps can automatically clean the drum by using UV lights to remove toner.
# Components
### Toner
Power bonded with pigment.
Black toner is typically carbon + polyester resin
### Toner Cartridge
![[Laser Printer-20240725024055569.webp|433]]
Supplies toner to apply to the page.
### Imaging Drum
![[Laser Printer-20240725022324613.webp|377]]
Aluminum cylinder coated with photosensitive compounds.
When light hits these compounds, electrical charge drains to the grounded cylinder, allowing it to apply toner onto the paper.
### Erase Lamp
![[Laser Printer-20240725023800147.webp|228]]
Applies light to the imaging drum.
### Primary Corona Wire / Primary Charge Roller
![[Laser Printer-20240725025320142.webp|287]]
Located close to the imaging drum.
Regulates and then passes voltage into the drum.
Ensures the drum can only receive 600-1000 Volts
### Transfer Corona Wire / Transfer Charge Roller
![[Laser Printer-20240725024933017.webp|368]]
Transferring image from drum to paper by attracting negatively charged toner particles to the positively charged page.
A static charge eliminator is then used to eliminate charge from the page.
Should be cleaned regularly with denatured alcohol
### Laser
![[Laser Printer-20240725024603764.webp]]
Writes onto the paper by sending charge to the imaging drum
### Fuser Assembly
![[Laser Printer-20240725025634786.webp]]
A pressure roller and heating roller are used to melt toner on the page so it can be fused permanently.
The heating roller uses [[Teflon]] to avoid toner sticking to it.
### Transfer Belt and Roller
![[Laser Printer-20240725022821229.webp|463]]
Used to pick up papers from the pickup roller
### Pickup Roller
![[Laser Printer-20240725023042745.webp|456]]
Used to grab 1 single page from paper storage or can be fed a paper directly.
Only 1 pages should be in the pickup roller at a time.
Should be cleaned often and replaced if the rollers become smooth
### Paper Storage
![[Laser Printer-20240725022736645.webp|406]]
The trays for blank papers.
![[Laser Printer-20240731021734156.webp|293]]
You can have multiple trays made for multiple paper types
### Separation Pad
![[Laser Printer-20240725023203723.webp|410]]
Small piece of rubber used to pick 1 page from the paper storage to feed into the pickup roller.
Very common to replace
### Gearbox
Used to provide the mechanical movements of the:
- Pickup roller
- Separation pad
- Fuser assembly
- Transfer roller
- Duplex system
### System Board
Electronic [[Printed Circuit Board|PCB]] containing:
- [[Read Only Memory|ROM]] for firmware
- [[Random Access Memory|RAM]] to store image before its printed
- [[Central Processing Unit|CPU]]
- Optional second [[Read Only Memory|ROM]] for new printer functionality in [[PostScript]]
You can add [[Single Inline Memory Module|SIMM]] or [[Dual Inline Memory Module|DIMM]] RAM for more image storage.
### Ozone Filter
The corona creates ozone which is harmful for printer components.
The ozone filter should be vacuumed regularly.
### Sensors and Switches
Sensors and switches are place throughout the printer to diagnose errors like:
- Paper jam
- Empty paper tray
- Low toner levels
# Additional Features
### Duplexing
Ability to print on both sides of page without human intervention.
Must print one side, turn page over and then print the second side.
### Calibration
To fix color issues in the printer and adjust toner usage
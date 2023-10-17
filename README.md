[![License](https://img.shields.io/badge/License-Apache2-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0) [![Community](https://img.shields.io/badge/Join-Community-blue)](https://developer.ibm.com/callforcode/solutions/projects/get-started/)

# Seamore

- [Project summary](#project-summary)
  - [The issue we are hoping to solve](#the-issue-we-are-hoping-to-solve)
  - [How our technology solution can help](#how-our-technology-solution-can-help)
  - [Our idea](#our-idea)
- [Technology implementation](#technology-implementation)
  - [IBM AI service(s) used](#ibm-ai-services-used)
  - [Other IBM technology used](#other-ibm-technology-used)
  - [Solution architecture](#solution-architecture)
- [Presentation materials](#presentation-materials)
  - [Solution demo video](#solution-demo-video)
  - [Project development roadmap](#project-development-roadmap)
- [Additional details](#additional-details)
  - [How to run the project](#how-to-run-the-project)
  - [Live demo](#live-demo)
- [About this template](#about-this-template)
  - [Contributing](#contributing)
  - [Versioning](#versioning)
  - [Authors](#authors)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)


## Project summary

### The issue we are hoping to solve

Seamore aims to address the critical issue of rapidly deteriorating ocean health and biodiversity due to various factors such as climate change, overfishing, and pollution. By providing real-time data on marine species, ocean pollution, coral reef health, and other vital parameters, Seamore seeks to enable informed decision-making and foster sustainable practices to mitigate these challenges. Through its comprehensive approach to ocean exploration and conservation, Seamore endeavors to contribute significantly to the preservation and protection of marine ecosystems worldwide.

### How our technology solution can help

Seamore: Real-time ocean data for informed conservation and management.

### Our idea
What's Up with this water ????

Seamore was conceived in response to the escalating environmental challenges faced by our oceans, which are experiencing unprecedented stress due to climate change, overfishing, and pollution. These factors collectively threaten the delicate balance of marine ecosystems and jeopardize the biodiversity crucial to the sustenance of life on our planet. Recognizing the urgency of the situation, our team embarked on a mission to develop an integrated solution that would harness the power of advanced technology to monitor, analyze, and protect our oceans.

At the heart of Seamore are intelligent Machine Learning models built into a network of autonomous underwater vehicles called Seabots. These Seabots operate seamlessly, collecting a wide array of vital data, including information on ocean pollutants, marine biodiversity, coral reef health, and key oceanic parameters such as temperature and pH levels. The data collected by the Seabot network is then meticulously mapped onto a globe interface, ensuring accessibility for anyone seeking to understand and utilize this comprehensive and real-time information for the benefit of oceanic research and conservation efforts.

The existing methods of ocean monitoring and data collection often suffer from limitations such as human resource constraints, sporadic data acquisition, and insufficient coverage. Seamore represents a significant leap forward in addressing these challenges by offering a comprehensive and continuous approach to ocean observation and analysis. Unlike traditional techniques that rely on infrequent sampling, Seamore's real-time monitoring capabilities provide a continuous stream of data, enabling a more holistic understanding of the dynamic changes occurring in our oceans. By delivering accurate and timely information, Seamore empowers stakeholders, including researchers, policymakers, and environmental organizations, to proactively respond to emerging threats and implement effective strategies for marine ecosystem preservation.

Moreover, Seamore's integrated approach serves as a significant improvement over existing solutions by offering a multifaceted perspective on ocean health. By combining the detection of pollutants, monitoring of marine life, and assessment of coral reef health, Seamore provides a comprehensive overview of the various interrelated factors influencing the well-being of marine ecosystems. This holistic approach is crucial for developing targeted conservation measures, implementing sustainable fishing practices, and advocating for the protection of vulnerable marine species and habitats.

In essence, Seamore represents a pioneering technological solution that is poised to revolutionize the field of ocean exploration and conservation. By leveraging the capabilities of advanced robotics and data analytics, Seamore is dedicated to safeguarding the health and resilience of our oceans, ensuring the preservation of marine biodiversity for future generations. Through collaborative efforts and a shared commitment to environmental stewardship, Seamore aims to foster a global movement toward sustainable ocean management and a more secure future for our planet's most vital ecosystem.

More detail is available in our [website](https://www.seamore.earth/).

## Technology implementation

### IBM AI service(s) used

- IBM Watson Machine Learning - model inference (see inference server)

### Other IBM technology used

- IBM Cloud Object Storage - Computer vision models and data collected from the seabot network

### Solution architecture

Diagram and step-by-step description of the flow of our solution:

![Video transcription/translaftion app](https://developer.ibm.com/developer/tutorials/cfc-starter-kit-speech-to-text-app-example/images/cfc-covid19-remote-education-diagram-2.png)

1. The user navigates to the site and uploads a video file.
2. Watson Speech to Text processes the audio and extracts the text.
3. Watson Translation (optionally) can translate the text to the desired language.
4. The app stores the translated text as a document within Object Storage.

## Presentation materials

_INSTRUCTIONS: The following deliverables should be officially posted to your My Team > Submissions section of the [Call for Code Global Challenge resources site](https://cfc-prod.skillsnetwork.site/), but you can also include them here for completeness. Replace the examples seen here with your own deliverable links._

### Solution demo video

[![Watch the video](https://raw.githubusercontent.com/Liquid-Prep/Liquid-Prep/main/images/readme/IBM-interview-video-image.png)](https://youtu.be/vOgCOoy_Bx0)

### Project development roadmap

The project currently does the following things.

- Feature 1
- Feature 2
- Feature 3

In the future we plan to...

See below for our proposed schedule on next steps after Call for Code 2023 submission.

![Roadmap](./images/roadmap.jpg)

## Additional details

_INSTRUCTIONS: The following deliverables are suggested, but **optional**. Additional details like this can help the judges better review your solution. Remove any sections you are not using._

### How to run the project

INSTRUCTIONS: In this section you add the instructions to run your project on your local machine for development and testing purposes. You can also add instructions on how to deploy the project in production.

### Live demo

You can find a running system to test at...

See our [description document](./docs/DESCRIPTION.md) for log in credentials.

---

_INSTRUCTIONS: You can remove the below section from your specific project README._

## About this template

### Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

### Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

### Authors

<a href="https://github.com/Call-for-Code/Project-Sample/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=Call-for-Code/Project-Sample" />
</a>

- **Billie Thompson** - _Initial work_ - [PurpleBooth](https://github.com/PurpleBooth)

### License

This project is licensed under the Apache 2 License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- Based on [Billie Thompson's README template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2).

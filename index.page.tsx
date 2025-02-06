// Learn more about how to build React pages in Realm: https://redocly.com/docs/realm/extend/how-to/create-react-page
import React from 'react';
import styled from 'styled-components';
import { Button } from '@redocly/theme';
import { Card } from '@redocly/theme/markdoc/components/Cards/Card';
import { Cards } from '@redocly/theme/markdoc/components/Cards/Cards';

// Import icons
import tutorialsIcon from './assets/site/icons/tutorials.svg';
import pythonSdkIcon from './assets/site/icons/python-sdk.svg';
import jsSdkIcon from './assets/site/icons/js-sdk.svg';
import taskWorkflowsIcon from './assets/site/icons/task-workflows.svg';
import faasIcon from './assets/site/icons/faas.svg';
import annotationsIcon from './assets/site/icons/annotations.svg';
import applicationsIcon from './assets/site/icons/applications.svg';
import analyticsIcon from './assets/site/icons/analytics.svg';

export default function HomePage() {
  return (
    <div>
      <HeroContainer>
        <HeroBg />
        <h1>Dataloop Developers Portal</h1>
        <p>A developer portal for beginners and advanced users</p>
        <Button 
          size="large" 
          variant="primary" 
          tone="brand" 
          to="/tutorials/getting_started/sdk_overview/chapter"
        >
          Get started
        </Button>
      </HeroContainer>

      <Container>
        <h3>Featured Resources</h3>
        <Cards>
          <Card 
            title="Tutorials" 
            to="/tutorials/tutorials"
            icon={tutorialsIcon}
          >
            Step-by-step guides to get started with Dataloop
          </Card>
          <Card 
            title="Python SDK" 
            to="https://sdk-docs.dataloop.ai/en/latest/_modules/index.html"
            icon={pythonSdkIcon}
          >
            Comprehensive Python SDK documentation and examples
          </Card>
          <Card 
            title="JavaScript SDK" 
            to="/resources/dtljs/index"
            icon={jsSdkIcon}
          >
            JavaScript SDK for web applications
          </Card>
        </Cards>
      </Container>

      <Container>
        <h3>Popular Topics</h3>
        <Cards>
          <Card 
            title="Task Workflows" 
            to="/tutorials/task_workflows"
            icon={taskWorkflowsIcon}
          >
            Learn about task creation and management
          </Card>
          <Card 
            title="FaaS" 
            to="/tutorials/faas"
            icon={faasIcon}
          >
            Function as a Service tutorials and guides
          </Card>
          <Card 
            title="Annotations" 
            to="/tutorials/annotations"
            icon={annotationsIcon}
          >
            Working with different types of annotations
          </Card>
          <Card 
            title="Applications" 
            to="/tutorials/applications"
            icon={applicationsIcon}
          >
            Building applications with Dataloop
          </Card>
          <Card 
            title="Analytics" 
            to="/tutorials/analytics"
            icon={analyticsIcon}
          >
            Data analytics and insights
          </Card>
        </Cards>
      </Container>

      <Container>
        <ContactUsSection>
          <h3>Need help?</h3>
          <ButtonContainer>
            <Button 
              variant="outlined" 
              size="large"
              to="https://docs.dataloop.ai/docs/help-getting-started"
            >
              Visit FAQ
            </Button>
            <Button 
              variant="outlined" 
              size="large"
              to="https://dataloop.ai/contact"
            >
              Contact us
            </Button>
          </ButtonContainer>
        </ContactUsSection>
      </Container>
    </div>
  );
}

const HeroBg = styled.div`
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;

  &:before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-size: cover;
    opacity: 0.7;
  }
  
  &:after {
    content: '';
    position: absolute;
    inset: 0;
    background-size: cover;
    opacity: 0.2;
  }
`;

const HeroContainer = styled.div`
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 32px;
  position: relative;

  h1 {
    color: var(--color-primary);
    text-align: center;
    font-size: 48px;
    font-weight: 700;
    line-height: 56px;
    margin: 80px 0 24px 0;
  }

  > p {
    color: var(--text-color-primary);
    text-align: center;
    font-size: 20px;
    font-weight: 600;
    line-height: 28px;
    margin: 0 0 24px 0;
  }
`;

const Container = styled.div`
  margin-top: 64px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  color: var(--text-color-secondary);
  font-size: 20px;
  font-weight: 400;
  line-height: 28px;
  width: min(90%, 886px);
  margin: 64px auto 0;

  a {
    text-decoration: none;
  }

  h3 {
    color: var(--text-color-primary);
    font-size: 24px;
    font-weight: 600;
    line-height: 32px;
    margin: 0 0 24px 0;
  }
`;

const ButtonContainer = styled.div`
  display: flex;
  gap: var(--spacing-xs);
  justify-content: center;
  flex-wrap: wrap;
`;

const ContactUsSection = styled.div`
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  margin-bottom: var(--spacing-lg);
  flex-wrap: wrap;
  gap: var(--spacing-xs);
  
  h3 {
    margin: 0;
  }
`;
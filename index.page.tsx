import React from 'react';
import styled from 'styled-components';
import tutorialsIcon from './assets/site/icons/tutorials.svg';
import onboardingIcon from './assets/site/icons/onboarding.svg';
import resourcesIcon from './assets/site/icons/resources.svg';
import { ArrowRightIcon, Button } from '@redocly/theme';
import { CardWithCode } from './@theme/components/CardWithCode/CardWithCode';
import { Card } from '@redocly/theme/markdoc/components/Cards/Card';
import { Cards } from '@redocly/theme/markdoc/components/Cards/Cards';

const Container = styled.div`
  padding: 2rem;
`;

const Header = styled.div`
  text-align: center;
  margin-bottom: 3rem;
`;

const Title = styled.h1`
  font-size: 2.5rem;
  margin-bottom: 1rem;
`;

const Subtitle = styled.h2`
  font-size: 1.5rem;
  font-weight: normal;
  margin-bottom: 2rem;
`;

interface HomePageProps {
  location: {
    pathname: string;
    search: string;
    hash: string;
  };
}

export default function HomePage({ location }: HomePageProps) {
  return (
    <Container>
      <Header>
        <Title>Dataloop Developers Portal</Title>
        <Subtitle>A developer portal for beginners and advanced users</Subtitle>
        <Button variant="outlined" size="xlarge" to="tutorials/getting_started/sdk_overview/chapter.md">
          Get started <ArrowRightIcon />
        </Button>
      </Header>
      <Cards>
        <Card title="Tutorials" to="tutorials/tutorials.mdx" icon={tutorialsIcon}>
          Step-by-step guides to get started with Dataloop
        </Card>
        <Card title="Onboarding" to="onboarding/onboarding.md" icon={onboardingIcon}>
          Get up and running with Dataloop platform
        </Card>
        <Card title="Resources" to="resources/resources.mdx" icon={resourcesIcon}>
          SDKs, APIs and developer tools
        </Card>
      </Cards>
    </Container>
  );
}


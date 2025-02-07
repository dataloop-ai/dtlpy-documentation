import React from 'react';
import styled from 'styled-components';
import pythonSdkIcon from '../assets/site/icons/python-sdk.svg';
import jsSdkIcon from '../assets/site/icons/js-sdk.svg';
import restApiIcon from '../assets/site/icons/rest-api.svg';

type CardWithCodeProps = {
  title: string;
  description: string;
  icon: string;
  onClick: () => void;
};

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
  color: var(--text-color);
`;

const Subtitle = styled.h2`
  font-size: 1.5rem;
  font-weight: normal;
  margin-bottom: 2rem;
  color: var(--text-color-secondary);
`;

const CardWrapper = styled.div`
  cursor: pointer;
  padding: 16px;
  background-color: var(--layer-color-ontonal);
  border-radius: 8px;
  transition: transform 0.2s, box-shadow 0.2s;
  margin-bottom: 16px;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
`;

const TopRow = styled.div`
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;

  img {
    width: 32px;
    height: 32px;
  }

  h4 {
    margin: 0;
    color: var(--text-color);
    font-size: 20px;
    font-weight: 600;
  }
`;

const Description = styled.p`
  margin: 0;
  color: var(--text-color-secondary);
  font-size: 16px;
  line-height: 24px;
`;

const CardsGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  padding: 1rem;
`;

const DlCard = ({ title, description, icon, onClick }: CardWithCodeProps) => {
  return (
    <CardWrapper onClick={onClick}>
      <TopRow>
        <img src={icon} alt={title} />
        <h4>{title}</h4>
      </TopRow>
      <Description>{description}</Description>
    </CardWrapper>
  );
};

const ResourcesPage = () => (
  <Container>
    <Header>
      <Title>Developer Resources & APIs 🛠️</Title>
      <Subtitle>
        Everything you need to build powerful AI applications
      </Subtitle>
    </Header>
    <CardsGrid>
      <DlCard
        title="Python SDK"
        description="Master our powerful Python SDK! Complete documentation and API reference for building robust AI applications 🐍"
        icon={pythonSdkIcon}
        onClick={() => window.location.href = 'https://sdk-docs.dataloop.ai/en/latest/_modules/index.html'}
      />
      <DlCard
        title="JavaScript SDK"
        description="Build dynamic web applications with our JavaScript SDK. Full API reference and interactive examples ⚡"
        icon={jsSdkIcon}
        onClick={() => window.location.href = '/resources/dtljs'}
      />
      <DlCard
        title="REST API"
        description="Direct access to Dataloop's API endpoints. Perfect for custom integrations and advanced workflows 🔌"
        icon={restApiIcon}
        onClick={() => window.location.href = 'https://gate.dataloop.ai/api/v1/docs'}
      />
    </CardsGrid>
  </Container>
);

export default ResourcesPage;
